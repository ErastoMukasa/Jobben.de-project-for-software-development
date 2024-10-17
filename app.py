from flask import Flask, render_template, request, redirect, url_for, session, flash 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError
import os
from werkzeug.utils import secure_filename
from flask_paginate import Pagination, get_page_parameter

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:6AHope@db/jobben_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Configure file upload
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Job model
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text, nullable=False)
    latitude = db.Column(db.Float, nullable=True)   # Added latitude
    longitude = db.Column(db.Float, nullable=True)  # Added longitude

    def __repr__(self):
        return f'<Job {self.title}>'

# Application model
class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    message = db.Column(db.Text, nullable=False)
    resume_filename = db.Column(db.String(150), nullable=False)

    job = db.relationship('Job', backref=db.backref('applications', lazy=True))

    def __repr__(self):
        return f'<Application {self.name}>'

# Create admin user if it does not exist
def create_admin_user():
    with app.app_context():
        admin_username = 'admin'
        admin_password = 'admin_password'  # Change to a strong password

        admin = User.query.filter_by(username=admin_username).first()
        if not admin:
            hashed_password = generate_password_hash(admin_password, method='pbkdf2:sha256')
            admin = User(username=admin_username, password=hashed_password)
            db.session.add(admin)
            db.session.commit()
            print('Admin user created successfully.')

# Flask-Login user loader
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))  # Updated for SQLAlchemy 2.0

# Routes
@app.route('/')
def index():
    search_query = request.args.get('search_query', '')
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 3

    if search_query:
        jobs_query = Job.query.filter(Job.location.ilike(f'%{search_query}%')).order_by(Job.id.desc())
    else:
        jobs_query = Job.query.order_by(Job.id.desc())

    pagination = jobs_query.paginate(page=page, per_page=per_page, error_out=False)
    return render_template('index.html', jobs=pagination, search_query=search_query)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        flash(f'Thank you, {name}. Your message has been sent!', 'success')
        return redirect(url_for('contact'))
        
    return render_template('contact.html')

@app.route('/job/<int:job_id>', methods=['GET', 'POST'])
def job_detail(job_id):
    job = Job.query.get_or_404(job_id)
    
    if request.method == 'POST':
        if not current_user.is_authenticated:
            flash('You need to be logged in to apply for a job.', 'danger')
            return redirect(url_for('login'))

        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        resume = request.files['resume']

        if resume and allowed_file(resume.filename):
            filename = secure_filename(resume.filename)
            resume_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            resume.save(resume_path)

            application = Application(
                job_id=job.id,
                name=name,
                email=email,
                message=message,
                resume_filename=filename
            )
            db.session.add(application)
            db.session.commit()

            flash('Your application has been submitted successfully!', 'success')

            return render_template('job_detail.html', job=job)

        flash('Invalid file format. Only PDF files are allowed.', 'danger')
    
    return render_template('job_detail.html', job=job)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup/job_seeker', methods=['GET', 'POST'])
def signup_job_seeker():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password)
        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('index'))
        except IntegrityError:
            db.session.rollback()
            flash('Username already exists', 'danger')
    return render_template('signup_job_seeker.html')

@app.route('/signup/employer', methods=['GET', 'POST'])
def signup_employer():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password)
        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('index'))
        except IntegrityError:
            db.session.rollback()
            flash('Username already exists', 'danger')
    return render_template('signup_employer.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = User.query.filter_by(username=username).first()
        if admin and check_password_hash(admin.password, password):
            session['logged_in'] = True
            return redirect(url_for('admin_panel'))
        flash('Invalid credentials', 'danger')
    return render_template('admin_login.html')

@app.route('/admin/panel')
@login_required
def admin_panel():
    if not session.get('logged_in'):
        return redirect(url_for('admin_login'))
    jobs = Job.query.all()
    admins = User.query.all()
    return render_template('admin.html', jobs=jobs, admins=admins)

@app.route('/admin/add', methods=['POST'])
@login_required
def add_job():
    if not session.get('logged_in'):
        return redirect(url_for('admin_login'))
    title = request.form.get('title')
    company = request.form.get('company')
    location = request.form.get('location')
    salary = request.form.get('salary')
    description = request.form.get('description')
    latitude = request.form.get('latitude')  # Added latitude
    longitude = request.form.get('longitude')  # Added longitude

    new_job = Job(title=title, company=company, location=location, salary=salary, description=description,
                  latitude=latitude, longitude=longitude)  # Updated Job creation
    db.session.add(new_job)
    db.session.commit()
    return redirect(url_for('admin_panel'))

@app.route('/admin/edit/<int:job_id>', methods=['POST'])
@login_required
def edit_job(job_id):
    if not session.get('logged_in'):
        return redirect(url_for('admin_login'))
    job = Job.query.get_or_404(job_id)
    job.title = request.form.get('title')
    job.company = request.form.get('company')
    job.location = request.form.get('location')
    job.salary = request.form.get('salary')
    job.description = request.form.get('description')
    job.latitude = request.form.get('latitude')  # Added latitude
    job.longitude = request.form.get('longitude')  # Added longitude

    db.session.commit()
    return redirect(url_for('admin_panel'))

@app.route('/admin/delete/<int:job_id>', methods=['POST'])
@login_required
def delete_job(job_id):
    if not session.get('logged_in'):
        return redirect(url_for('admin_login'))
    job = Job.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    return redirect(url_for('admin_panel'))

if __name__ == '__main__':
    create_admin_user()
    app.run(debug=True)
