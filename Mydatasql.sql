-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
SHOW WARNINGS;
-- -----------------------------------------------------
-- Schema schooldb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `schooldb` ;

-- -----------------------------------------------------
-- Schema schooldb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `schooldb` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
SHOW WARNINGS;
USE `schooldb` ;

-- -----------------------------------------------------
-- Table `examtype_master_tbl`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `examtype_master_tbl` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `examtype_master_tbl` (
  `Section` INT NOT NULL,
  `Exam` VARCHAR(15) NOT NULL,
  `Subject` VARCHAR(22) NOT NULL,
  `Max_marks` INT NOT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `student_acad_tbl`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `student_acad_tbl` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `student_acad_tbl` (
  `Student_Id` CHAR(7) NOT NULL,
  `Session` CHAR(9) NOT NULL,
  `Exam` VARCHAR(15) NOT NULL,
  `Sub_1A` INT NULL DEFAULT NULL,
  `Sub_1B` INT NULL DEFAULT NULL,
  `Sub_2A` INT NULL DEFAULT NULL,
  `Sub_2B` INT NULL DEFAULT NULL,
  `Sub_3A` INT NULL DEFAULT NULL,
  `Sub_3B` INT NULL DEFAULT NULL,
  `Sub_4A` INT NULL DEFAULT NULL,
  `Sub_4B` INT NULL DEFAULT NULL,
  `Sub_5A` INT NULL DEFAULT NULL,
  `Sub_5B` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Student_Id`, `Session`, `Exam`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `student_assgn_tbl`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `student_assgn_tbl` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `student_assgn_tbl` (
  `Section` INT NOT NULL DEFAULT '0',
  `Division` CHAR(1) NOT NULL DEFAULT 'N',
  `Assgnt_Date` DATE NOT NULL,
  `Subject` VARCHAR(20) NOT NULL DEFAULT 'Default',
  `Topic` VARCHAR(45) NOT NULL,
  `Assignment_Link` LONGBLOB NOT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `subject_master_tbl`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `subject_master_tbl` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `subject_master_tbl` (
  `Course_Code` VARCHAR(6) NOT NULL,
  `Sub1` VARCHAR(20) NOT NULL,
  `Sub2` VARCHAR(20) NOT NULL,
  `Sub3` VARCHAR(20) NOT NULL,
  `Sub4` VARCHAR(20) NOT NULL,
  `Sub5` VARCHAR(20) NOT NULL,
  `Sub6` VARCHAR(20) NULL DEFAULT NULL,
  `Sub7` VARCHAR(20) NULL DEFAULT NULL,
  `Sub8` VARCHAR(20) NULL DEFAULT NULL,
  `Sub9` VARCHAR(20) NULL DEFAULT NULL,
  `Fees` INT NOT NULL,
  PRIMARY KEY (`Course_Code`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `student_master_tbl`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `student_master_tbl` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `student_master_tbl` (
  `Student_ID` CHAR(7) NOT NULL,
  `First_name` VARCHAR(20) NOT NULL,
  `Last_name` VARCHAR(20) NOT NULL,
  `Password` VARCHAR(15) NOT NULL,
  `Father_Name` VARCHAR(15) NOT NULL,
  `Mother_Name` VARCHAR(15) NOT NULL,
  `Standard` INT NOT NULL,
  `Division` CHAR(1) NULL DEFAULT NULL,
  `Roll` INT NULL DEFAULT NULL,
  `Course` VARCHAR(6) NOT NULL,
  `DOB` VARCHAR(10) NULL DEFAULT '2005-12-01',
  `House` VARCHAR(10) NULL DEFAULT NULL,
  `Gender` VARCHAR(6) NOT NULL,
  `Blood_Group` VARCHAR(2) NOT NULL,
  `Phone_Number` VARCHAR(11) NOT NULL,
  `Address_L1` VARCHAR(50) NOT NULL,
  `Address_L2` VARCHAR(50) NOT NULL,
  `Address_L3` VARCHAR(50) NOT NULL,
  `City` VARCHAR(28) NOT NULL,
  `Pincode` CHAR(8) NOT NULL,
  `Status` CHAR(1) NOT NULL,
  `School_Session` CHAR(9) NULL DEFAULT NULL,
  `Due_Amt` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Student_ID`),
  CONSTRAINT `Course_C`
    FOREIGN KEY (`Course`)
    REFERENCES `subject_master_tbl` (`Course_Code`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;
CREATE INDEX `Course_Code_idx` ON `student_master_tbl` (`Course` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `student_attend_tbl`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `student_attend_tbl` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `student_attend_tbl` (
  `Student_Id` CHAR(7) NULL DEFAULT NULL,
  `Date1` DATE NULL DEFAULT NULL,
  `Day1` VARCHAR(9) NULL DEFAULT NULL,
  `Attendance` VARCHAR(1) NULL DEFAULT NULL,
  CONSTRAINT `fk_studentID`
    FOREIGN KEY (`Student_Id`)
    REFERENCES `student_master_tbl` (`Student_ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;
CREATE INDEX `fk_studentID` ON `student_attend_tbl` (`Student_Id` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `student_attend_tbl_old`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `student_attend_tbl_old` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `student_attend_tbl_old` (
  `Student_Id` CHAR(7) NOT NULL,
  `Date1` DATE NOT NULL,
  `Day` VARCHAR(9) NULL DEFAULT NULL,
  `Attendance` CHAR(1) NULL DEFAULT NULL,
  PRIMARY KEY (`Student_Id`, `Date1`),
  CONSTRAINT `Id_Stud`
    FOREIGN KEY (`Student_Id`)
    REFERENCES `student_master_tbl` (`Student_ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;
CREATE INDEX `Student_Id_idx` ON `student_attend_tbl_old` (`Student_Id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `Stu_Id_idx` ON `student_attend_tbl_old` (`Student_Id` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `student_notice_tbl`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `student_notice_tbl` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `student_notice_tbl` (
  `Circular_no` CHAR(8) NOT NULL,
  `Title` VARCHAR(45) NOT NULL,
  `Notice_Date` DATE NOT NULL,
  `Text` LONGBLOB NOT NULL,
  PRIMARY KEY (`Circular_no`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `teacher_master_tbl`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `teacher_master_tbl` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `teacher_master_tbl` (
  `Teacher_ID` CHAR(7) NOT NULL,
  `First_name` VARCHAR(20) NOT NULL,
  `Last_name` VARCHAR(20) NOT NULL,
  `Password` VARCHAR(15) NOT NULL,
  `Classes` CHAR(8) NOT NULL,
  `Subject` VARCHAR(20) NOT NULL,
  `DOB` DATE NOT NULL,
  `House` VARCHAR(10) NULL DEFAULT NULL,
  `Gender` VARCHAR(6) NOT NULL,
  `Blood_Group` VARCHAR(2) NOT NULL,
  `Phone_Number` VARCHAR(11) NOT NULL,
  `Address_L1` VARCHAR(50) NOT NULL,
  `Address_L2` VARCHAR(50) NOT NULL,
  `Address_L3` VARCHAR(50) NOT NULL,
  `City` VARCHAR(28) NOT NULL,
  `Pincode` CHAR(8) NOT NULL,
  `Status` CHAR(1) NOT NULL,
  PRIMARY KEY (`Teacher_ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;
USE `schooldb`;

DELIMITER $$

USE `schooldb`$$
DROP TRIGGER IF EXISTS `new_record` $$
SHOW WARNINGS$$
USE `schooldb`$$
CREATE
DEFINER=`root`@`localhost`
TRIGGER `schooldb`.`new_record`
AFTER INSERT ON `schooldb`.`student_master_tbl`
FOR EACH ROW
BEGIN
		INSERT INTO student_attend_tbl SET Student_Id=NEW.Student_ID;
	END$$

SHOW WARNINGS$$

USE `schooldb`$$
DROP TRIGGER IF EXISTS `student_master_tbl_BEFORE_INSERT` $$
SHOW WARNINGS$$
USE `schooldb`$$
CREATE
DEFINER=`root`@`localhost`
TRIGGER `schooldb`.`student_master_tbl_BEFORE_INSERT`
BEFORE INSERT ON `schooldb`.`student_master_tbl`
FOR EACH ROW
SET NEW.Due_Amt=(select subject_master_tbl.Fees
    from subject_master_tbl where new.Course=subject_master_tbl.Course_Code)$$

SHOW WARNINGS$$

DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
