# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:16:03 2024

@author: ADMIN
"""


import mysql.connector as sqltor
import Editor
import pickle

file = open(r"Password_data.dat", "rb")
Pwds = pickle.load(file)
file.close()

Schooldb = sqltor.connect(
    host=Pwds["Sql_data"]["host"],
    user=Pwds["Sql_data"]["user"],
    password=Pwds["Sql_data"]["password"],
    database=Pwds["Sql_data"]["database"],
    auth_plugin="mysql_native_password",
)


def Id_Check(User):
    try:
        cursor = Schooldb.cursor()
        if User == "Student":
            Query = """select Student_Id,Status from student_master_tbl WHERE Status!='N'"""
        elif User == "Teacher":
            Query = """select Teacher_Id from teacher_master_tbl WHERE Status!='N'"""
        cursor.execute(Query)
        result = cursor.fetchall()
        Data = []

        for x in result:
            Data.append(str(x[0]))
    except:
        return None

    else:
        return Data


def Dataset_Retriever(Id, User):
    try:
        if User == "Student":
            Query = """SELECT Status FROM student_master_tbl WHERE Student_Id = %s"""
            cursor = Schooldb.cursor()
            cursor.execute(Query, (Id,))
            result = cursor.fetchall()[0][0]
            if result == "X":
                print("Account has not been Activated Yet")
                return None
            elif result == "N":
                print("Account Deleted")
                return None
            Query = """select * from student_master_tbl where 
            Status = 'A' AND Student_Id = %s"""
            cursor.execute(Query, (Id,))
            result = cursor.fetchall()[0]
            result = list(result)
            Query = """select Sub1,Sub2,Sub3,Sub4,Sub5,Sub6,Sub7,
            Sub8,Sub9 from subject_master_tbl where Course_Code= %s"""
            cursor.execute(Query, (result[9],))
            result[9] = cursor.fetchmany(1)[0]

        elif User == "Teacher":
            cursor = Schooldb.cursor()
            Query = """select * from teacher_master_tbl where 
            Status = 'A' AND Teacher_Id = %s"""
            cursor.execute(Query, (Id,))
            result = cursor.fetchall()[0]
            result = list(result)

        elif User == "Student_Teacher":
            cursor = Schooldb.cursor()

            Query = (
                """select * from student_master_tbl where Student_Id = %s"""
            )
            cursor.execute(Query, (Id,))
            result = cursor.fetchall()[0]
            result = list(result)
            Query = """select Sub1,Sub2,Sub3,Sub4,Sub5,Sub6,Sub7,
            Sub8,Sub9 from subject_master_tbl where Course_Code= %s"""
            cursor.execute(Query, (result[9],))
            result[9] = cursor.fetchmany(1)[0]

    except:
        print("System Error. Please Wait")
        return None
    else:
        return result


def Data_Delete(Id, Mode):
    try:
        cursor = Schooldb.cursor()
        if Mode == "Student":
            Query = """ 
                    UPDATE student_master_tbl
                    SET Status = 'N' 
                    where Status = 'A' AND Student_Id = %s"""
        elif Mode == "Staff":
            Query = """ 
                    UPDATE teacher_master_tbl
                    SET Status = 'N' 
                    where Status = 'A' AND Teacher_Id = %s"""
        cursor.execute(Query, (Id,))
        Schooldb.commit()

    except:
        print("System Error. Please Wait")


def New_Entree(Data, Mode):
    cursor = Schooldb.cursor()
    print(Data)
    if Mode == "Student":
        Query = """ 
                INSERT INTO student_master_tbl 
                (Student_ID, First_name, Last_name, Password, 
                 Father_Name, Mother_Name, Standard, Division, Roll, 
                 Course, DOB, House, Gender, Blood_Group, 
                 Phone_Number, Address_L1, Address_L2, Address_L3, 
                 City, Pincode,School_Session, Status)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                        %s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    elif Mode == "Staff":
        Query = """ 
                INSERT INTO teacher_master_tbl (Teacher_ID, 
                First_name, Last_name, Password, Classes, Subject,
                DOB, House, Gender, Blood_Group, Phone_Number,
                Address_L1, Address_L2, Address_L3, City, Pincode, 
                Status)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                        %s,%s,%s,%s)"""
    cursor.execute(Query, Data)
    Schooldb.commit()

    print("System Error. Please Wait")


def Pwd_Updater(Id, Pass, User):
    try:
        cursor = Schooldb.cursor()
        if User == "Student":
            Query = """ 
                    UPDATE student_master_tbl
                    SET Password = %s 
                    where Status = 'A' AND Student_Id = %s"""
        elif User == "Teacher":
            Query = """ 
                    UPDATE teacher_master_tbl
                    SET Password = %s 
                    where Status = 'A' AND Teacher_Id = %s"""

        cursor.execute(Query, (Pass, Id))
        Schooldb.commit()

    except:
        print("System Error. Please Wait")


def Assgn_data(Id):
    try:
        cursor = Schooldb.cursor()
        Query = """select Standard,Division from student_master_tbl 
        where Status = 'A' AND Student_Id = %s"""
        cursor.execute(Query, (Id,))
        Class = list(cursor.fetchall()[0])
        Query = """select Assgnt_Date,Topic,Assignment_Link 
        from student_assgn_tbl where Section= %s AND Division= %s"""
        cursor.execute(Query, (Class[0], Class[1]))
        result = list(cursor.fetchall())

        for x in result:
            record = x
            result[result.index(x)] = list(x)
            result[result.index(list(record))][2] = list(record)[2].decode(
                "utf-8"
            )
    except:
        print("System Error. Please Wait")
        return None
    else:
        return result


def update_assgn(Id, Sec, Div, Date, Topic, Link, Mode):
    if Mode == "Add":
        cursor = Schooldb.cursor()
        Query = """select Subject from teacher_master_tbl 
                    where Status = 'A' AND Teacher_Id = %s"""
        cursor.execute(Query, (Id,))
        Subject = cursor.fetchall()[0][0]
        Query = """INSERT INTO student_assgn_tbl 
                    (Section, Division, Assgnt_Date,Subject,Topic ,Assignment_Link)
                    VALUES (%s,%s,%s,%s,%s,%s) """
        cursor.execute(
            Query,
            (
                Sec,
                Div,
                Date,
                Subject,
                Topic,
                Link.encode("utf-8"),
            ),
        )
        Schooldb.commit()

    elif Mode == "View":
        cursor = Schooldb.cursor()
        Query = """select Subject from teacher_master_tbl 
                            where Status = 'A' AND Teacher_Id = %s"""
        cursor.execute(Query, (Id,))
        Subject = cursor.fetchall()[0][0]
        Query = """select Assgnt_Date,Topic,Assignment_Link 
                        from student_assgn_tbl where Subject= %s"""
        cursor.execute(Query, (Subject,))
        result = list(cursor.fetchall())

        for x in result:
            record = x
            result[result.index(x)] = list(x)
            result[result.index(list(record))][2] = list(record)[2].decode(
                "utf-8"
            )

        return result


def Notice():
    cursor = Schooldb.cursor()
    Query = """ 
                Select Notice_Date, Title, Text 
                FROM student_notice_tbl ORDER BY Notice_Date"""
    cursor.execute(
        Query,
    )
    result = list(cursor.fetchall())
    for x in result:
        record = x
        result[result.index(x)] = list(x)
        result[result.index(list(record))][2] = list(record)[2].decode("utf-8")
    return result


def Notice_Add(Circle_no, Title, Dte, Text):
    cursor = Schooldb.cursor()
    Query = """INSERT INTO student_notice_tbl 
            (Circular_no, Title, Notice_Date, Text)
            VALUES (%s,%s,%s,%s) """
    cursor.execute(Query, (Circle_no, Title, Dte, Text.encode("utf_8")))
    Schooldb.commit()


def Attendance(Mth, Id):
    cursor = Schooldb.cursor()
    Query = """select Date1, Day1, Attendance from student_attend_tbl 
    where Month(Date1)= %s AND Student_Id = %s"""
    cursor.execute(Query, (Mth, Id))
    query_result = cursor.fetchall()
    result = []

    for i in range(len(query_result) - 1):
        result.append(list(query_result[i]))
        if result[i][2] == "1":
            result[i][2] = "P"
        elif result[i][2] == "0":
            result[i][2] = "Ab"
        elif result[i][2] == "":
            result[i][2] = "-"
    return result


def Marksheet(Exam, Id, Sec, Sub, Session):
    cursor = Schooldb.cursor()
    Query = """select Subject, Max_Marks 
    from examtype_master_tbl 
    where Section=%s  AND Exam = %s"""

    cursor.execute(Query, (Sec, Exam))
    Max = cursor.fetchall()
    Subject_log = []
    while None in Sub or "" in Sub:
        if None in Sub:
            Sub.remove(None)
        elif "" in Sub:
            Sub.remove("")
    for i in range(len(Sub)):
        for x in Max:
            if x[0].startswith(Sub[i]):
                Subject_log.append([x[0], x[1], (x[1] * 33 // 100)])

    Query = """select Sub_1A,Sub_1B,Sub_2A,Sub_2B
    ,Sub_3A,Sub_3B,Sub_4A,Sub_4B,Sub_5A,Sub_5B 
    from student_acad_tbl 
    where Student_Id = %s AND Session = %s AND Exam = %s"""

    cursor.execute(Query, (Id, Session, Exam))
    query_result = cursor.fetchall()

    marks = []
    for i in range(len(query_result)):
        marks.append(list(query_result[i]))
        for orig in marks:
            new = orig
            for item in new:
                if item == 0 or item == None:
                    del new[new.index(item)]
            marks[marks.index(orig)] = new

    for i in range(len(Subject_log)):
        Subject_log[i].append(marks[0][i])

    for i in range(len(Subject_log)):
        Subject_log[i].append(Editor.Grader(Subject_log[i]))
    return Subject_log


def Exam(Sec):
    cursor = Schooldb.cursor()
    Query = (
        """select DISTINCT Exam from examtype_master_tbl where Section= %s"""
    )
    cursor.execute(Query, (Sec,))
    result = cursor.fetchall()
    Exam = []
    for x in result:
        Exam.append(list(x))
    return Exam


def Override(Id):
    cursor = Schooldb.cursor()

    Query = """select Password from student_master_tbl where 
                Student_Id = %s"""
    cursor.execute(Query, (Id,))
    result = cursor.fetchall()[0][0]
    return result


def End():
    try:
        cursor = Schooldb.cursor()
        cursor.flush()
        cursor.close()
        Schooldb.close()
    except:
        pass
    else:
        Schooldb.close()


# End()
