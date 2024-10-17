"""Create user table

Revision ID: 8516a02d294d
Revises: 67865ba2a8d0
Create Date: 2024-08-25 19:10:20.305502

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8516a02d294d'
down_revision = '67865ba2a8d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    with op.batch_alter_table('job', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=150),
               existing_nullable=False)
        batch_op.alter_column('company',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=150),
               existing_nullable=False)
        batch_op.alter_column('location',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=150),
               existing_nullable=False)
        batch_op.alter_column('salary',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=150),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('job', schema=None) as batch_op:
        batch_op.alter_column('salary',
               existing_type=sa.String(length=150),
               type_=mysql.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('location',
               existing_type=sa.String(length=150),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.alter_column('company',
               existing_type=sa.String(length=150),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.alter_column('title',
               existing_type=sa.String(length=150),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)

    op.drop_table('user')
    # ### end Alembic commands ###
