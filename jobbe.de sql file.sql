-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping data for table jobben_database.alembic_version: ~1 rows (approximately)
INSERT IGNORE INTO `alembic_version` (`version_num`) VALUES
	('4b72b837f5dc');

-- Dumping data for table jobben_database.application: ~21 rows (approximately)
INSERT IGNORE INTO `application` (`id`, `job_id`, `name`, `email`, `message`, `resume_filename`) VALUES
	(1, 4, 'Eraasito Mukasa', 'mukrasto@gmail.com', 'hghghg', 'Guidelines_Oral_Assignment_1.pdf'),
	(2, 4, 'Testing 3', 'mukrasto@gmail.com', 'my name', 'Guidelines_Oral_Assignment_1.pdf'),
	(3, 4, 'testing 4', 'mukrasto@gmail.com', 'sdasda', 'Guidelines_Oral_Assignment_1.pdf'),
	(4, 4, 'testing 5', 'mukrasto@gmail.com', 'sdasd', 'Guidelines_Oral_Assignment_1.pdf'),
	(5, 3, 'testing 5', 'mukrasto@gmail.com', 'hjhj', 'Guidelines_Oral_Assignment_1.pdf'),
	(6, 5, 'testing 5', 'mukrasto@gmail.com', 'asda', 'Guidelines_Oral_Assignment_1.pdf'),
	(7, 4, 'muky', 'mukrasto@gmail.com', 'xasss', 'Guidelines_Oral_Assignment_1.pdf'),
	(8, 4, 'muky', 'mukrasto@gmail.com', 'xasss', 'Guidelines_Oral_Assignment_1.pdf'),
	(9, 4, 'testing 6', 'mukrasto@gmail.com', 'nsbdnsb', 'Guidelines_Oral_Assignment_1.pdf'),
	(10, 5, 'testing 5', 'mukrasto@gmail.com', 'asa', 'Guidelines_Oral_Assignment_1.pdf'),
	(11, 5, 'testing 5', 'mukrasto@gmail.com', 'asa', 'Guidelines_Oral_Assignment_1.pdf'),
	(12, 5, 'testing 5', 'mukrasto@gmail.com', 'asa', 'Guidelines_Oral_Assignment_1.pdf'),
	(13, 5, 'testing 5', 'mukrasto@gmail.com', 'asa', 'Guidelines_Oral_Assignment_1.pdf'),
	(14, 5, 'testing 5', 'mukrasto@gmail.com', 'asa', 'Guidelines_Oral_Assignment_1.pdf'),
	(15, 5, 'testing 6', 'mukrasto@gmail.com', 'sjsj', 'Guidelines_Oral_Assignment_1.pdf'),
	(16, 5, 'testing 6', 'mukrasto@gmail.com', 'sjsj', 'Guidelines_Oral_Assignment_1.pdf'),
	(17, 5, 'testing 6', 'mukrasto@gmail.com', 'sjsj', 'Guidelines_Oral_Assignment_1.pdf'),
	(18, 5, 'testing 6', 'mukrasto@gmail.com', 'sjsj', 'Guidelines_Oral_Assignment_1.pdf'),
	(19, 5, 'testing 6', 'mukrasto@gmail.com', 'sjsj', 'Guidelines_Oral_Assignment_1.pdf'),
	(20, 5, 'testing 6', 'mukrasto@gmail.com', 'sjsj', 'Guidelines_Oral_Assignment_1.pdf'),
	(21, 4, 'testing 6', 'mukrasto@gmail.com', 'jhjss', 'Guidelines_Oral_Assignment_1.pdf');

-- Dumping data for table jobben_database.job: ~6 rows (approximately)
INSERT IGNORE INTO `job` (`id`, `title`, `company`, `location`, `salary`, `description`, `latitude`, `longitude`) VALUES
	(3, 'testing one', 'Grace Corps', 'siemensstadt', '5000', 'updated', 52.3215, 13.1528),
	(4, 'pot washer', 'jobben', 'postadmer', '3000', 'updated', NULL, NULL),
	(5, 'house help', 'Grace Corps', 'zoologisher', '5000', 'updated', NULL, NULL),
	(6, 'House Help', 'jobben', 'Postdamer Platz', '1000', 'To be updated', NULL, NULL),
	(7, 'Glass cleaner', 'jobben', 'Postdamer Platz', '3000', 'updated', 52.3984, 13.0657),
	(8, 'Office Cleaner', 'jobben', 'to be updated', '1000', 'updated', 52.5096, 13.3753);

-- Dumping data for table jobben_database.user: ~4 rows (approximately)
INSERT IGNORE INTO `user` (`id`, `username`, `password`) VALUES
	(1, 'testing one', 'test'),
	(3, 'Erasto', 'test2'),
	(4, 'admin', 'pbkdf2:sha256:600000$2s0xohdhrJehgatJ$dd919756f99699a103ede5d3f96498b754e9c14eaa1a04e706c500fd0008f4a6'),
	(6, 'Mukasa', 'pbkdf2:sha256:600000$1UgvN4UHLebxCPSj$d829ae23367bd181f07cd5f65fd15443275a18905de2f7dd8045074701a9d73c');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
