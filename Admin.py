# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:18:57 2024

@author: Student
"""
import Info
import PySimpleGUI as psg
import pickle
import datetime
import Profile
import Attendence
import Marksheet

file = open(r"Password_data.dat", "rb")
Pwds = pickle.load(file)
file.close()


def Admin_Access():
    Pass_check = psg.popup_get_text(
        "Enter password for access to admin servers: ",
        title="Password",
        password_char="*",
        font=(16),
    )

    if Pass_check == Pwds["Admin_Student"]:
        layout = [
            [
                psg.Text(
                    text="Admin Access",
                    font=("Arial Bold", 16),
                    size=20,
                    expand_x=True,
                    justification="center",
                )
            ],
            [
                psg.Button(
                    "Delete Student Data",
                    font=16,
                    auto_size_button=True,
                )
            ],
            [psg.Button("New Admission", font=16, auto_size_button=True)],
        ]

        secure_admin = psg.Window(
            "School MyClassroom",
            layout,
            finalize=True,
            resizable=False,
        )
        while True:
            event, values = secure_admin.read()
            if event == psg.WIN_CLOSED:
                secure_admin.close()
                break
            elif event == "Delete Student Data":
                Id = psg.popup_get_text(
                    "Enter student id to delete and archive: ",
                    title="Remove Student",
                    font=(16),
                )
                Info.Data_Delete(Id, "Student")
                secure_admin.close()
                break
            elif event == "New Admission":
                secure_admin.close()
                layout = [
                    [
                        psg.Text(
                            "Student Id ",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Text(
                            "First Name",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Text(
                            "Last Name ",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Text(
                            "Father's Name",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Text(
                            "Mother's Name",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Text(
                            "Class",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.OptionMenu(
                            values=[
                                12,
                                11,
                                10,
                                9,
                                8,
                                7,
                                6,
                                5,
                                4,
                                3,
                                2,
                                1,
                            ]
                        ),
                        psg.Text(
                            "Section",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.OptionMenu(values=["A", "B", "C", "D"]),
                    ],
                    [
                        psg.Text(
                            "Roll No:",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Text(
                            "Subject Combo",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.OptionMenu(
                            values=[
                                "A1101",
                                "A1102",
                                "B1103",
                                "B1104",
                                "B1105",
                                "B1106",
                                "C1107",
                                "C1108",
                                "D1109",
                                "D1110",
                                "D1111",
                            ]
                        ),
                    ],
                    [
                        psg.Input(key="_DOB_"),
                        psg.CalendarButton(
                            "Date Of Birth",
                            close_when_date_chosen=True,
                            target="_DOB_",
                            format="%Y-%m-%d",
                            font=(16),
                        ),
                    ],
                    [
                        psg.Text(
                            "House",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.OptionMenu(
                            values=[
                                "Ashoka",
                                "Kanishka",
                                "Pratap",
                                "Shivaji",
                            ]
                        ),
                        psg.Text(
                            "Gender",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.OptionMenu(values=["Female", "Male", "Other"]),
                    ],
                    [
                        psg.Text(
                            "Blood Group",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.OptionMenu(
                            values=[
                                "A+",
                                "A-",
                                "B+",
                                "B-",
                                "AB+",
                                "AB-",
                                "O+",
                                "O-",
                            ]
                        ),
                    ],
                    [
                        psg.Text(
                            "Phone Number",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Text(
                            "Address",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        )
                    ],
                    [psg.Input(expand_x=True, font=(16))],
                    [psg.Input(expand_x=True, font=(16))],
                    [psg.Input(expand_x=True, font=(16))],
                    [
                        psg.Text(
                            "City",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Text(
                            "Pincode",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Text(
                            "School Session",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Button("OK", font=16, auto_size_button=True),
                        psg.Button("Back", font=16, auto_size_button=True),
                    ],
                ]

                new_rec_admin = psg.Window(
                    "School MyClassroom",
                    layout,
                    finalize=True,
                    resizable=True,
                )
                while True:
                    event, values = new_rec_admin.read()
                    if event == psg.WIN_CLOSED:
                        new_rec_admin.close()
                        break

                    elif event == "OK":
                        Id = values[0]
                        Name_1 = values[1]
                        Name_2 = values[2]
                        Pwd = "Kharghar123"
                        F_Name = values[3]
                        M_Name = values[4]
                        Class = values[5]
                        Sec = values[6]
                        Roll = values[7]
                        Sub = values[8]
                        date = values["_DOB_"]
                        House = values[9]
                        Gen = values[10]
                        Group = values[11]
                        Num = values[12]
                        Add_1 = values[13]
                        Add_2 = values[14]
                        Add_3 = values[15]
                        City = values[16]
                        Code = values[17]
                        Session = values[18]
                        Status = "X"

                        DOB = []
                        for val in date.split("-"):
                            DOB.append(int(val))
                        DOB = datetime.date(DOB[0], DOB[1], DOB[2])

                        Student_Data = (
                            Id,
                            Name_1,
                            Name_2,
                            Pwd,
                            F_Name,
                            M_Name,
                            Class,
                            Sec,
                            Roll,
                            Sub,
                            date,
                            House,
                            Gen,
                            Group,
                            Num,
                            Add_1,
                            Add_2,
                            Add_3,
                            City,
                            Code,
                            Session,
                            Status,
                        )
                        Info.New_Entree(Student_Data, "Student")
                        new_rec_admin.close()
                        break

                    elif event == "Back":
                        new_rec_admin.close()
                        break
                break

    elif (
        Pass_check != Pwds["Admin_Student"]
        and Pass_check != Pwds["Admin_Staff"]
        and Pass_check != None
    ):
        psg.PopupQuickMessage("Wrong Password")

    elif Pass_check == Pwds["Admin_Staff"]:
        layout = [
            [
                psg.Text(
                    text="Admin Access",
                    font=("Arial Bold", 16),
                    size=20,
                    expand_x=True,
                    justification="center",
                )
            ],
            [
                psg.Button(
                    "Delete Staff Record",
                    font=16,
                    auto_size_button=True,
                )
            ],
            [
                psg.Button(
                    "New Staff Personnel",
                    font=16,
                    auto_size_button=True,
                )
            ],
        ]

        secure_admin = psg.Window(
            "School MyClassroom",
            layout,
            finalize=True,
            resizable=False,
        )
        while True:
            event, values = secure_admin.read()
            if event == psg.WIN_CLOSED:
                secure_admin.close()
            elif event == "Delete Staff Record":
                Id = psg.popup_get_text(
                    "Enter staff id to delete and archive: ",
                    title="Remove Staff",
                    font=(16),
                )
                Info.Data_Delete(Id, "Staff")
                secure_admin.close()
                break
            elif event == "New Staff Personnel":
                secure_admin.close()
                layout = [
                    [
                        psg.Text(
                            "Staff Id ",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Text(
                            "First Name",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Text(
                            "Last Name ",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Text(
                            "Classes",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Text(
                            "Subject",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Input(key="_DOB_"),
                        psg.CalendarButton(
                            "Date Of Birth",
                            close_when_date_chosen=True,
                            target="_DOB_",
                            format="%Y-%m-%d",
                            font=(16),
                        ),
                    ],
                    [
                        psg.Text(
                            "House",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.OptionMenu(
                            values=[
                                "Ashoka",
                                "Kanishka",
                                "Pratap",
                                "Shivaji",
                            ]
                        ),
                    ],
                    [
                        psg.Text(
                            "Gender",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.OptionMenu(values=["Female", "Male", "Other"]),
                    ],
                    [
                        psg.Text(
                            "Blood Group",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Text(
                            "Phone Number",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Text(
                            "Address",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        )
                    ],
                    [psg.Input(expand_x=True, font=(16))],
                    [psg.Input(expand_x=True, font=(16))],
                    [psg.Input(expand_x=True, font=(16))],
                    [
                        psg.Text(
                            "City",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Text(
                            "Pincode",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Button("OK", font=16, auto_size_button=True),
                        psg.Button("Back", font=16, auto_size_button=True),
                    ],
                ]

                new_rec_admin = psg.Window(
                    "School MyClassroom",
                    layout,
                    finalize=True,
                    resizable=True,
                )
                while True:
                    event, values = new_rec_admin.read()
                    if event == psg.WIN_CLOSED:
                        new_rec_admin.close()
                        break

                    elif event == "OK":
                        Id = values[0]
                        Name_1 = values[1]
                        Name_2 = values[2]
                        Pwd = "Kharghar123"
                        Class = values[3]
                        Sub = values[4]
                        DOB = values["_DOB_"]
                        House = values[5]
                        Gen = values[6]
                        Group = values[7]
                        Num = values[8]
                        Add_1 = values[9]
                        Add_2 = values[10]
                        Add_3 = values[11]
                        City = values[12]
                        Code = values[13]
                        Status = "A"

                        Staff_Data = (
                            Id,
                            Name_1,
                            Name_2,
                            Pwd,
                            Class,
                            Sub,
                            DOB,
                            House,
                            Gen,
                            Group,
                            Num,
                            Add_1,
                            Add_2,
                            Add_3,
                            City,
                            Code,
                            Status,
                        )
                        Info.New_Entree(Staff_Data, "Staff")
                        new_rec_admin.close()
                        break

                    elif event == "Back":
                        new_rec_admin.close()
                        break
                break

    elif Pass_check != Pwds["Admin_Student"] and Pass_check != None:
        psg.PopupQuickMessage("Wrong Password")

    else:
        pass
    return None


def Viewer(Id):
    Pass = Info.Override(Id)
    Student = Info.Dataset_Retriever(Id, "Student_Teacher")
    Pass_check = psg.popup_get_text(
        "Enter password for access to admin servers: ",
        title="Password",
        password_char="*",
        font=(16),
    )

    if Pass_check == Pwds["Admin_Student"]:
        layout = [
            [psg.Button("Profile Data", key="Profile")],
            [psg.Button("Attendance sheet", key="Register")],
            [psg.Button("Marksheet", key="Marks")],
        ]

        student_data_admin = psg.Window(
            "School MyClassroom",
            layout,
            finalize=True,
            resizable=False,
        )
        while True:
            event, values = student_data_admin.read()
            if event == psg.WIN_CLOSED:
                student_data_admin.close()
                break
            elif event == "Profile":
                layout_profile = Profile.DispProfile(Id, Pass, Student)

                Profile_data = psg.Window(
                    "School MyClassroom",
                    layout_profile,
                    finalize=True,
                    resizable=True,
                )
                while True:
                    event, values = Profile_data.read()
                    if event == psg.WIN_CLOSED:
                        Profile_data.close()
                        break
                continue
            elif event == "Register":
                layout_attend = [
                    [
                        psg.Text(
                            text="Attendence Sheet:",
                            font=("Arial Bold", 20),
                        )
                    ],
                    [Attendence.Disp(Id, Student)],
                ]
                Attend_data = psg.Window(
                    "School MyClassroom",
                    layout_attend,
                    finalize=True,
                    resizable=True,
                )
                while True:
                    event, values = Attend_data.read()
                    if event == psg.WIN_CLOSED:
                        Attend_data.close()
                        break
                continue

            elif event == "Marks":
                layout_marks = [
                    [
                        psg.Text(
                            text="MarkSheet:",
                            font=("Arial Bold", 20),
                        )
                    ],
                    [
                        Marksheet.Disp(
                            Info.Exam(str(Student[6])),
                            Id,
                            str(Student[6]),
                            list(Student[9]),
                            str(Student[21]),
                            Student,
                        )
                    ],
                ]
                Marksheet_data = psg.Window(
                    "School MyClassroom",
                    layout_marks,
                    finalize=True,
                    resizable=True,
                )
                while True:
                    event, values = Marksheet_data.read()
                    if event == psg.WIN_CLOSED:
                        Marksheet_data.close()
                        break
                continue
