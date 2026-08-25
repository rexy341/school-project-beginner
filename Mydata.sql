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

-- -----------------------------------------------------
-- Schema schooldb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `schooldb` DEFAULT CHARACTER SET utf8mb4 ;
SHOW WARNINGS;
USE `schooldb` ;

-- -----------------------------------------------------
-- Table `examtype_master_tbl`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `examtype_master_tbl` (
  `Section` INT(11) NOT NULL,
  `Exam` VARCHAR(15) NOT NULL,
  `Subject` VARCHAR(22) NOT NULL,
  `Max_marks` INT(11) NOT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `feesdate_master_tbl`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `feesdate_master_tbl` (
  `Quarter` CHAR(8) NOT NULL,
  `Last_Date` DATE NOT NULL,
  `Fine_Amount` INT(11) NOT NULL,
  PRIMARY KEY (`Quarter`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `student_acad_tbl`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `student_acad_tbl` (
  `Student_Id` CHAR(7) NOT NULL,
  `Session` CHAR(9) NOT NULL,
  `Exam` VARCHAR(15) NOT NULL,
  `Sub_1A` INT(11) NULL DEFAULT NULL,
  `Sub_1B` INT(11) NULL DEFAULT NULL,
  `Sub_2A` INT(11) NULL DEFAULT NULL,
  `Sub_2B` INT(11) NULL DEFAULT NULL,
  `Sub_3A` INT(11) NULL DEFAULT NULL,
  `Sub_3B` INT(11) NULL DEFAULT NULL,
  `Sub_4A` INT(11) NULL DEFAULT NULL,
  `Sub_4B` INT(11) NULL DEFAULT NULL,
  `Sub_5A` INT(11) NULL DEFAULT NULL,
  `Sub_5B` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`Student_Id`, `Session`, `Exam`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `student_assgn_tbl`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `student_assgn_tbl` (
  `Section` INT(11) NOT NULL DEFAULT '0',
  `Division` CHAR(1) NOT NULL DEFAULT 'N',
  `Assgnt_Date` DATE NOT NULL,
  `Subject` VARCHAR(20) NOT NULL DEFAULT 'Default',
  `Topic` VARCHAR(15) NOT NULL,
  `Assignment_Link` LONGBLOB NOT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `student_attend_tbl`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `student_attend_tbl` (
  `Student_Id` CHAR(7) NOT NULL,
  `Date` DATE NOT NULL DEFAULT '0000-00-00',
  `Day` VARCHAR(9) NULL DEFAULT NULL,
  `Attendance` CHAR(1) NULL DEFAULT NULL,
  PRIMARY KEY (`Student_Id`, `Date`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `subject_master_tbl`
-- -----------------------------------------------------
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
  `Fees` INT(11) NOT NULL,
  PRIMARY KEY (`Course_Code`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `student_master_tbl`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `student_master_tbl` (
  `Student_ID` CHAR(7) NOT NULL,
  `First_name` VARCHAR(20) NOT NULL,
  `Last_name` VARCHAR(20) NOT NULL,
  `Password` VARCHAR(15) NOT NULL,
  `Father_Name` VARCHAR(15) NOT NULL,
  `Mother_Name` VARCHAR(15) NOT NULL,
  `Standard` INT(11) NOT NULL,
  `Division` CHAR(1) NULL DEFAULT NULL,
  `Roll` INT(11) NULL DEFAULT NULL,
  `Course` VARCHAR(6) NOT NULL,
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
  `School_Session` CHAR(9) NULL DEFAULT NULL,
  `Due_Amt` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`Student_ID`),
  CONSTRAINT `Course_C`
    FOREIGN KEY (`Course`)
    REFERENCES `subject_master_tbl` (`Course_Code`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

SHOW WARNINGS;
CREATE INDEX `Course_Code_idx` ON `student_master_tbl` (`Course` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `student_fees_tbl`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `student_fees_tbl` (
  `Id` CHAR(7) NOT NULL,
  `Session` CHAR(9) NOT NULL,
  `Quarter` CHAR(8) NOT NULL,
  `Date_of_payment` DATE NULL DEFAULT NULL,
  `Amount` INT(11) NOT NULL,
  `Fine` INT(11) NULL DEFAULT NULL,
  `MISC_Fees` INT(11) NULL DEFAULT NULL,
  `Mode_of_payment` VARCHAR(15) NULL DEFAULT NULL,
  PRIMARY KEY (`Id`, `Quarter`),
  CONSTRAINT `Quarter`
    FOREIGN KEY (`Quarter`)
    REFERENCES `feesdate_master_tbl` (`Quarter`),
  CONSTRAINT `StudentId`
    FOREIGN KEY (`Id`)
    REFERENCES `student_master_tbl` (`Student_ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

SHOW WARNINGS;
CREATE INDEX `Quarter_idx` ON `student_fees_tbl` (`Quarter` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `student_notice_tbl`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `student_notice_tbl` (
  `Circular_no` CHAR(8) NOT NULL,
  `Title` VARCHAR(45) NOT NULL,
  `Notice_Date` DATE NOT NULL,
  `Text` LONGBLOB NOT NULL,
  PRIMARY KEY (`Circular_no`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `teacher_master_tbl`
-- -----------------------------------------------------
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
DEFAULT CHARACTER SET = utf8mb4;

SHOW WARNINGS;
USE `schooldb`;

DELIMITER $$
SHOW WARNINGS$$
USE `schooldb`$$
CREATE
DEFINER=`root`@`localhost`
TRIGGER `schooldb`.`student_fees_tbl_AFTER_INSERT`
AFTER INSERT ON `schooldb`.`student_fees_tbl`
FOR EACH ROW
BEGIN
	UPDATE student_master_tbl
    SET Due_Amt=Due_Amt-NEW.Amount
    WHERE Student_ID = NEW.Id;
END$$

SHOW WARNINGS$$

DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
