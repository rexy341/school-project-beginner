# -*- coding: utf-8 -*-

try:
    import PySimpleGUI as psg  # Module for implementation of GUI
except:
    print(
        "Your system does not possess the requirements for running this application"
    )
import Info
import Editor
import Notice
import Profile
import Assignment
import webbrowser
import pickle
import Attendence
import Marksheet
import Admin

psg.theme("TealMono")
Id = ""
Pass = ""
while True:
    layout = [
        [
            psg.Text(
                text="ClassroomConnect",
                font=("Arial Bold", 16),
                size=20,
                expand_x=True,
                justification="center",
            )
        ],
        [
            psg.Text(
                text="Which Mode do you wish to use:",
                font=("Arial Bold", 16),
                expand_x=True,
            )
        ],
        [psg.Radio("Student", group_id=0000, font=("Arial Bold", 16))],
        [psg.Radio("Teacher", group_id=0000, font=("Arial Bold", 16))],
        [psg.Button("OK", font=16)],
    ]
    window = psg.Window(
        "School MyClassroom",
        layout,
        size=(715, 250),
        finalize=True,
        resizable=False,
    )
    while True:
        event, values = window.read()
        if event == psg.WIN_CLOSED:
            window.close()
            Info.End()
            Editor.End()
        elif event == "Back":
            window.close()
            break
        elif "OK" in event:
            window.close()
            if values[0] == True:
                layout = [
                    [
                        psg.Text(
                            text="ClassroomConnect",
                            font=("Arial Bold", 16),
                            size=20,
                            expand_x=True,
                            justification="center",
                        )
                    ],
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
                            "Password ",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(
                            expand_x=True,
                            password_char="*",
                            font=(16),
                        ),
                    ],
                    [
                        psg.Button("OK", font=16, auto_size_button=True),
                        psg.Button("Back", font=16, auto_size_button=True),
                    ],
                ]
                wnd = psg.Window(
                    "School MyClassroom",
                    layout,
                    size=(715, 250),
                    finalize=True,
                )
                while True:
                    event, values = wnd.read()
                    if event == psg.WIN_CLOSED:
                        wnd.close()
                        Info.End()
                        Editor.End()
                        break
                    elif event == "Back":
                        wnd.close()
                        break
                    elif "OK" in event:
                        User = "Student"
                        if (
                            values[0] in (Info.Id_Check(User))
                            or values[0] == Id
                        ):
                            Student = Info.Dataset_Retriever(values[0], User)
                            if Student == None:
                                wnd.close()
                                Info.End()
                                Editor.End()
                                break
                            Id = values[0]
                            Pass = Student[3]
                            if values[1] == Pass:
                                wnd.close()

                                file = open(r"AboutUs.dat", "rb")
                                List = [
                                    [
                                        psg.Image(
                                            filename="School.png",
                                            size=[300, 200],
                                        )
                                    ],
                                    [psg.VPush()],
                                    [
                                        psg.Listbox(
                                            Editor.Menu(User),
                                            enable_events=True,
                                            no_scrollbar=True,
                                            font=(
                                                "Arial Bold",
                                                20,
                                            ),
                                            size=(12, 8),
                                        )
                                    ],
                                    [
                                        psg.Button("Home", font=16),
                                        psg.Button("Logout", font=16),
                                        psg.Button(
                                            "Change Password",
                                            enable_events=True,
                                            font=16,
                                            key="_Pwd_",
                                        ),
                                    ],
                                ]
                                Page = [
                                    [
                                        psg.Text(
                                            text="WELCOME!",
                                            font=("Arial Bold", 30),
                                            justification="left",
                                        )
                                    ],
                                    [psg.Push()],
                                    [
                                        psg.Image(
                                            filename="School.png",
                                            size=[400, 250],
                                        )
                                    ],
                                ]
                                Assign_pg = [
                                    [
                                        psg.Text(
                                            text="Your Assignments :",
                                            font=("Arial Bold", 20),
                                        )
                                    ],
                                    [psg.VPush()],
                                    [Assignment.stud_work(Id)[0]],
                                    [psg.VPush()],
                                ]
                                Notice_pg = [
                                    [
                                        psg.Text(
                                            text="Your Notices :",
                                            font=("Arial Bold", 20),
                                        )
                                    ],
                                    [psg.VPush()],
                                    [
                                        psg.Input(
                                            key="_Search_",
                                            do_not_clear=False,
                                        )
                                    ],
                                    [
                                        psg.CalendarButton(
                                            "Search by date",
                                            close_when_date_chosen=True,
                                            target="_Search_",
                                            format="%Y-%m-%d",
                                            font=(16),
                                        )
                                    ],
                                    [
                                        psg.Button("OK", font=(16)),
                                        psg.Button("Back", font=(16)),
                                    ],
                                    [psg.VPush()],
                                    [Notice.Disp(Info.Notice())[0]],
                                ]
                                About_Us_pg = [
                                    [
                                        psg.Text(
                                            text=str(pickle.load(file)),
                                            font=("Arial Bold", 16),
                                            justification="center",
                                        )
                                    ]
                                ]

                                Attend_pg = [
                                    [
                                        psg.Text(
                                            text="Attendence Sheet:",
                                            font=("Arial Bold", 20),
                                        )
                                    ],
                                    [Attendence.Disp(Id, Student)],
                                ]

                                Marks_pg = [
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
                                Main_pg = [
                                    [
                                        psg.Frame(
                                            "MyClassroom",
                                            Page,
                                            size=(1000, 1600),
                                            expand_x=True,
                                            expand_y=True,
                                            element_justification="center",
                                        )
                                    ]
                                ]
                                Profile_disp = [
                                    [
                                        psg.Frame(
                                            "Profile",
                                            Profile.DispProfile(
                                                Id, Pass, Student
                                            ),
                                            size=(1000, 1600),
                                        )
                                    ]
                                ]
                                Assign = [
                                    [
                                        psg.Frame(
                                            "Assignment",
                                            Assign_pg,
                                            size=(1000, 1600),
                                        )
                                    ]
                                ]
                                Notice_disp = [
                                    [
                                        psg.Frame(
                                            "Notice",
                                            Notice_pg,
                                            size=(1000, 1600),
                                        )
                                    ]
                                ]
                                About = [
                                    [
                                        psg.Frame(
                                            "About Us",
                                            About_Us_pg,
                                            size=(1100, 1600),
                                        )
                                    ]
                                ]
                                Attend_disp = [
                                    [
                                        psg.Frame(
                                            "Attendence",
                                            Attend_pg,
                                            size=(1000, 1600),
                                        )
                                    ]
                                ]
                                Marks_disp = [
                                    [
                                        psg.Frame(
                                            "Marksheet",
                                            Marks_pg,
                                            size=(1000, 1600),
                                        )
                                    ]
                                ]

                                layout = [
                                    [
                                        psg.Column(
                                            List,
                                        ),
                                        psg.VSeperator(),
                                        psg.Column(
                                            Profile_disp,
                                            visible=False,
                                            key="_Profile_",
                                        ),
                                        psg.Column(
                                            About,
                                            visible=False,
                                            key="_AboutUs_",
                                            scrollable=True,
                                        ),
                                        psg.Column(
                                            Assign,
                                            visible=False,
                                            key="_Assign_",
                                        ),
                                        psg.Column(
                                            Notice_disp,
                                            visible=False,
                                            key="_NoticePg_",
                                        ),
                                        psg.Column(
                                            Main_pg,
                                            visible=True,
                                            key="_Main_",
                                        ),
                                        psg.Column(
                                            Attend_disp,
                                            visible=False,
                                            key="_AttendPg_",
                                        ),
                                        psg.Column(
                                            Marks_disp,
                                            visible=False,
                                            key="_MarksPg_",
                                        ),
                                    ]
                                ]
                                window = psg.Window(
                                    "School MyClassroom",
                                    layout,
                                    finalize=True,
                                    resizable=True,
                                )
                                window.Maximize()
                                file.close()
                                while True:
                                    event, values = window.read()
                                    if event == psg.WIN_CLOSED:
                                        window.close()
                                        Info.End()
                                        Editor.End()
                                    elif event == "Logout":
                                        window.close()
                                        break

                                    elif event == "_Pwd_":
                                        Editor.UpdatePass(Id, Pass, User)
                                        continue

                                    elif event == "Home":
                                        window["_Main_"].update(visible=True)
                                        window["_Profile_"].update(
                                            visible=False
                                        )
                                        window["_AboutUs_"].update(
                                            visible=False
                                        )
                                        window["_Assign_"].update(
                                            visible=False
                                        )
                                        window["_NoticePg_"].update(
                                            visible=False
                                        )
                                        window["_AttendPg_"].update(
                                            visible=False
                                        )
                                        window["_MarksPg_"].update(
                                            visible=False
                                        )

                                        continue

                                    elif values[1] == ["Profile"]:
                                        window["_Profile_"].update(
                                            visible=True
                                        )
                                        window["_Main_"].update(visible=False)
                                        window["_AboutUs_"].update(
                                            visible=False
                                        )
                                        window["_Assign_"].update(
                                            visible=False
                                        )
                                        window["_NoticePg_"].update(
                                            visible=False
                                        )
                                        window["_AttendPg_"].update(
                                            visible=False
                                        )
                                        window["_MarksPg_"].update(
                                            visible=False
                                        )
                                        continue

                                    elif values[1] == ["Assignments"]:
                                        window["_Main_"].update(visible=False)
                                        window["_NoticePg_"].update(
                                            visible=False
                                        )
                                        window["_AboutUs_"].update(
                                            visible=False
                                        )
                                        window["_Profile_"].update(
                                            visible=False
                                        )
                                        window["_Assign_"].update(visible=True)
                                        window["_AttendPg_"].update(
                                            visible=False
                                        )
                                        window["_MarksPg_"].update(
                                            visible=False
                                        )

                                        if event == "_TABLE_":
                                            rows = Assignment.stud_work(Id)[1]
                                            url = rows[(values["_TABLE_"])[0]][
                                                2
                                            ]
                                            webbrowser.open(url)
                                        continue

                                    elif values[1] == ["Notice"]:
                                        window["_Main_"].update(visible=False)
                                        window["_Assign_"].update(
                                            visible=False
                                        )
                                        window["_AboutUs_"].update(
                                            visible=False
                                        )
                                        window["_Profile_"].update(
                                            visible=False
                                        )
                                        window["_NoticePg_"].update(
                                            visible=True
                                        )
                                        window["_AttendPg_"].update(
                                            visible=False
                                        )
                                        window["_MarksPg_"].update(
                                            visible=False
                                        )

                                        if event == "OK":
                                            Date = values["_Search_"].split()
                                            if Date != []:
                                                if (
                                                    Editor.validate(
                                                        str(Date[0])
                                                    )
                                                    == -1
                                                ):
                                                    search_result = []
                                                    for x in Info.Notice():
                                                        if str(x[0]) == str(
                                                            Date[0]
                                                        ):
                                                            search_result.append(
                                                                x
                                                            )
                                                    window["_Notice_"].update(
                                                        values=search_result
                                                    )
                                            else:
                                                pass

                                        if event == "Back":
                                            window["_Notice_"].update(
                                                values=Info.Notice()
                                            )

                                        if (
                                            event == "_Notice_"
                                            and values["_Notice_"] != []
                                        ):
                                            rows = Info.Notice()
                                            notice = rows[
                                                (values["_Notice_"])[0]
                                            ][2]
                                            psg.popup_no_buttons(notice)
                                        continue

                                    elif values[1] == ["Attendence"]:
                                        window["_Main_"].update(visible=False)
                                        window["_Assign_"].update(
                                            visible=False
                                        )
                                        window["_Profile_"].update(
                                            visible=False
                                        )
                                        window["_NoticePg_"].update(
                                            visible=False
                                        )
                                        window["_AboutUs_"].update(
                                            visible=False
                                        )
                                        window["_AttendPg_"].update(
                                            visible=True
                                        )
                                        window["_MarksPg_"].update(
                                            visible=False
                                        )
                                        continue

                                    elif values[1] == ["Marksheet"]:
                                        window["_Main_"].update(visible=False)
                                        window["_Assign_"].update(
                                            visible=False
                                        )
                                        window["_Profile_"].update(
                                            visible=False
                                        )
                                        window["_NoticePg_"].update(
                                            visible=False
                                        )
                                        window["_AboutUs_"].update(
                                            visible=False
                                        )
                                        window["_AttendPg_"].update(
                                            visible=False
                                        )
                                        window["_MarksPg_"].update(
                                            visible=True
                                        )
                                        continue

                                    elif values[1] == ["About Us"]:
                                        window["_Main_"].update(visible=False)
                                        window["_Assign_"].update(
                                            visible=False
                                        )
                                        window["_Profile_"].update(
                                            visible=False
                                        )
                                        window["_NoticePg_"].update(
                                            visible=False
                                        )
                                        window["_AttendPg_"].update(
                                            visible=False
                                        )
                                        window["_AboutUs_"].update(
                                            visible=True
                                        )
                                        window["_MarksPg_"].update(
                                            visible=False
                                        )
                                        continue
                                    else:
                                        window.close()
                                        break
                                break
                            else:
                                print("Password Wrong")
                                psg.PopupQuickMessage("Wrong Password")
                                wnd.close()
                                break
                        elif Info.Id_Check(User) == None:
                            print("Database Server Error")
                            wnd.close()
                            Info.End()
                            file.close()
                            Editor.End()
                            break
                        else:
                            print("Student Id wrong")
                            wnd.close()
                            break
                    break
            elif values[1] == True:
                layout = [
                    [
                        psg.Text(
                            text="ClassroomConnect",
                            font=("Arial Bold", 16),
                            size=20,
                            expand_x=True,
                            justification="center",
                        )
                    ],
                    [
                        psg.Text(
                            "Teacher Id ",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(expand_x=True, font=(16)),
                    ],
                    [
                        psg.Text(
                            "Password ",
                            font=("Arial Bold", 16),
                            size=(15, 1),
                        ),
                        psg.Input(
                            expand_x=True,
                            password_char="*",
                            font=(16),
                        ),
                    ],
                    [
                        psg.Button("OK", font=16, auto_size_button=True),
                        psg.Button("Back", font=16, auto_size_button=True),
                    ],
                ]
                wnd = psg.Window(
                    "School MyClassroom",
                    layout,
                    size=(715, 250),
                    finalize=True,
                )
                while True:
                    event, values = wnd.read()
                    if event == psg.WIN_CLOSED:
                        wnd.close()
                        Info.End()
                        Editor.End()
                    elif event == "Back":
                        wnd.close()
                        break
                    elif "OK" in event:
                        User = "Teacher"
                        if (
                            values[0] in (Info.Id_Check(User))
                            or values[0] == Id
                        ):
                            Teacher = Info.Dataset_Retriever(values[0], User)
                            Id = values[0]
                            Pass = Teacher[3]
                            if values[1] == Pass:
                                wnd.close()
                                file = open(r"AboutUs.dat", "rb")
                                List = [
                                    [
                                        psg.Image(
                                            filename="School.png",
                                            size=[300, 200],
                                        )
                                    ],
                                    [psg.VPush()],
                                    [
                                        psg.Listbox(
                                            Editor.Menu(User),
                                            enable_events=True,
                                            no_scrollbar=True,
                                            font=(
                                                "Arial Bold",
                                                20,
                                            ),
                                            size=(12, 10),
                                        )
                                    ],
                                    [
                                        psg.Button("Home", font=16),
                                        psg.Button("Logout", font=16),
                                        psg.Button(
                                            "Change Password",
                                            enable_events=True,
                                            font=16,
                                            key="_Pwd_",
                                        ),
                                    ],
                                ]
                                Page = [
                                    [
                                        psg.Text(
                                            text="WELCOME!",
                                            font=(
                                                "Arial Bold",
                                                30,
                                            ),
                                            justification="left",
                                        )
                                    ],
                                    [psg.Push()],
                                    [
                                        psg.Image(
                                            filename="School.png",
                                            size=[400, 250],
                                        )
                                    ],
                                ]

                                Assign_pg = [
                                    [
                                        psg.Text(
                                            text="Assignment Records :",
                                            font=(
                                                "Arial Bold",
                                                20,
                                            ),
                                        )
                                    ],
                                    [psg.VPush()],
                                    [
                                        psg.Button(
                                            "Create new asignment",
                                            font=16,
                                            key="_new-assgn_",
                                        )
                                    ],
                                    [psg.VPush()],
                                    [
                                        Assignment.teacher_work(
                                            Id,
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "View",
                                        )[0]
                                    ],
                                    [psg.VPush()],
                                ]

                                Notice_pg = [
                                    [
                                        psg.Text(
                                            text="Notice Records :",
                                            font=(
                                                "Arial Bold",
                                                20,
                                            ),
                                        )
                                    ],
                                    [psg.VPush()],
                                    [
                                        psg.Button(
                                            "Enter new circular",
                                            font=16,
                                            key="_new-notice_",
                                        )
                                    ],
                                    [
                                        psg.Button(
                                            "Reload",
                                            font=16,
                                            key="_back_",
                                        )
                                    ],
                                    [psg.VPush()],
                                    [Notice.Disp(Info.Notice())[0]],
                                    [psg.VPush()],
                                ]
                                Admin_pg = [
                                    [psg.Push()],
                                    [
                                        psg.Radio(
                                            "Student Data",
                                            group_id=0000,
                                            font=(
                                                "Arial Bold",
                                                16,
                                            ),
                                            key="_Admin-keys_",
                                        )
                                    ],
                                    [
                                        psg.Radio(
                                            "School Administration",
                                            group_id=0000,
                                            font=(
                                                "Arial Bold",
                                                16,
                                            ),
                                        )
                                    ],
                                    [psg.Button("OK", font=16)],
                                    [psg.VPush()],
                                ]

                                Data_access = [
                                    [psg.VPush()],
                                    [psg.Push()],
                                    [
                                        psg.Text(
                                            text="Student Data",
                                            font=(
                                                "Arial Bold",
                                                30,
                                            ),
                                            justification="center",
                                        )
                                    ],
                                    [
                                        psg.Text(
                                            "Student Id ",
                                            font=(
                                                "Arial Bold",
                                                16,
                                            ),
                                            size=(15, 1),
                                        ),
                                        psg.Input(
                                            expand_x=True,
                                            do_not_clear=False,
                                            font=(16),
                                        ),
                                    ],
                                    [
                                        psg.Button(
                                            "OK",
                                            font=16,
                                            auto_size_button=True,
                                        )
                                    ],
                                    [psg.VPush()],
                                ]

                                Main_pg = [
                                    [
                                        psg.Frame(
                                            "MyClassroom",
                                            Page,
                                            size=(1000, 1600),
                                            expand_x=True,
                                            expand_y=True,
                                            element_justification="center",
                                        )
                                    ]
                                ]
                                Profile_disp = [
                                    [
                                        psg.Frame(
                                            "Profile",
                                            Profile.DispProfile_T(
                                                Id, Pass, Teacher
                                            ),
                                            size=(1000, 1600),
                                        )
                                    ]
                                ]
                                Admin_disp = [
                                    [
                                        psg.Frame(
                                            "Admin Page",
                                            Admin_pg,
                                            size=(1000, 1600),
                                        )
                                    ]
                                ]

                                Assign = [
                                    [
                                        psg.Frame(
                                            "Assignment",
                                            Assign_pg,
                                            size=(1000, 1600),
                                        )
                                    ]
                                ]

                                Notices = [
                                    [
                                        psg.Frame(
                                            "Notices",
                                            Notice_pg,
                                            size=(1000, 1600),
                                        )
                                    ]
                                ]

                                Data_disp = [
                                    [
                                        psg.Frame(
                                            "Student Data",
                                            Data_access,
                                            size=(1000, 1600),
                                        )
                                    ]
                                ]

                                layout = [
                                    [
                                        psg.Column(
                                            List,
                                        ),
                                        psg.VSeperator(),
                                        psg.Column(
                                            Profile_disp,
                                            visible=False,
                                            key="_Profile_",
                                        ),
                                        psg.Column(
                                            Main_pg,
                                            visible=True,
                                            key="_Main_",
                                        ),
                                        psg.Column(
                                            Assign,
                                            visible=False,
                                            key="_Assgn_",
                                        ),
                                        psg.Column(
                                            Admin_disp,
                                            visible=False,
                                            key="_Admin_",
                                        ),
                                        psg.Column(
                                            Data_disp,
                                            visible=False,
                                            key="_Data_",
                                        ),
                                        psg.Column(
                                            Notices,
                                            visible=False,
                                            key="_Not_",
                                        ),
                                    ]
                                ]
                                window = psg.Window(
                                    "School MyClassroom",
                                    layout,
                                    finalize=True,
                                    resizable=True,
                                )
                                window.Maximize()
                                file.close()
                                while True:
                                    event, values = window.read()
                                    if event == psg.WIN_CLOSED:
                                        window.close()
                                        Info.End()
                                        Editor.End()
                                    elif event == "Logout":
                                        window.close()
                                        break

                                    elif event == "_Pwd_":
                                        Editor.UpdatePass(Id, Pass, User)
                                        continue

                                    elif event == "Home":
                                        window["_Main_"].update(visible=True)
                                        window["_Profile_"].update(
                                            visible=False
                                        )
                                        window["_Admin_"].update(visible=False)
                                        window["_Data_"].update(visible=False)
                                        window["_Assgn_"].update(visible=False)

                                        window["_Not_"].update(visible=False)

                                        continue

                                    elif values[1] == ["Profile"]:
                                        window["_Profile_"].update(
                                            visible=True
                                        )

                                        window["_Main_"].update(visible=False)
                                        window["_Admin_"].update(visible=False)

                                        window["_Data_"].update(visible=False)

                                        window["_Assgn_"].update(visible=False)
                                        window["_Not_"].update(visible=False)

                                    elif values[1] == ["Admin Access"]:
                                        window["_Profile_"].update(
                                            visible=False
                                        )

                                        window["_Admin_"].update(visible=True)
                                        window["_Main_"].update(visible=False)

                                        window["_Data_"].update(visible=False)

                                        window["_Assgn_"].update(visible=False)

                                        window["_Not_"].update(visible=False)

                                        if values["_Admin-keys_"] == True:
                                            Admin.Admin_Access()
                                            window[
                                                "_Admin-keys_"
                                            ].reset_group()

                                        elif values[5] == True:
                                            Admin.Admin_Access()
                                            window[
                                                "_Admin-keys_"
                                            ].reset_group()
                                        continue

                                    elif values[1] == ["Assignments"]:
                                        window["_Profile_"].update(
                                            visible=False
                                        )

                                        window["_Admin_"].update(visible=False)
                                        window["_Main_"].update(visible=False)

                                        window["_Data_"].update(visible=False)

                                        window["_Assgn_"].update(visible=True)
                                        window["_Not_"].update(visible=False)

                                        if event == "_new-assgn_":
                                            layout_new_assgn = [
                                                [
                                                    psg.Input(
                                                        key="_TODAY_",
                                                    ),
                                                    psg.CalendarButton(
                                                        "Enter date",
                                                        close_when_date_chosen=True,
                                                        target="_TODAY_",
                                                        format="%Y-%m-%d",
                                                        font=(16),
                                                    ),
                                                ],
                                                [
                                                    psg.Text(
                                                        "Enter section: ",
                                                        font=(
                                                            "Arial Bold",
                                                            16,
                                                        ),
                                                    ),
                                                    psg.OptionMenu(
                                                        values=[
                                                            12,
                                                            11,
                                                        ]
                                                    ),
                                                ],
                                                [
                                                    psg.Text(
                                                        "Enter division: ",
                                                        font=(
                                                            "Arial Bold",
                                                            16,
                                                        ),
                                                    ),
                                                    psg.OptionMenu(
                                                        values=[
                                                            "A",
                                                            "B",
                                                            "C",
                                                            "D",
                                                        ]
                                                    ),
                                                ],
                                                [
                                                    psg.Text(
                                                        "Enter Topic ",
                                                        font=(
                                                            "Arial Bold",
                                                            16,
                                                        ),
                                                        size=(15, 1),
                                                    ),
                                                    psg.Input(
                                                        expand_x=True,
                                                        font=(16),
                                                    ),
                                                ],
                                                [
                                                    psg.Text(
                                                        "Enter Link ",
                                                        font=(
                                                            "Arial Bold",
                                                            16,
                                                        ),
                                                        size=(15, 1),
                                                    ),
                                                    psg.Input(
                                                        expand_x=True,
                                                        font=(
                                                            "Arial Bold",
                                                            16,
                                                        ),
                                                    ),
                                                ],
                                                [
                                                    psg.Button(
                                                        "OK",
                                                        font=16,
                                                        auto_size_button=True,
                                                    ),
                                                    psg.Button(
                                                        "Back",
                                                        font=16,
                                                        auto_size_button=True,
                                                    ),
                                                ],
                                            ]

                                            wnd = psg.Window(
                                                "School MyClassroom",
                                                layout_new_assgn,
                                                size=(715, 250),
                                                finalize=True,
                                            )
                                            while True:
                                                (
                                                    event,
                                                    values,
                                                ) = wnd.read()
                                                if event == psg.WIN_CLOSED:
                                                    wnd.close()
                                                    break
                                                elif event == "Back":
                                                    wnd.close()
                                                    break
                                                elif "OK" in event:
                                                    Info.update_assgn(
                                                        Id,
                                                        values[0],
                                                        values[1],
                                                        values["_TODAY_"],
                                                        values[2],
                                                        values[3],
                                                        "Add",
                                                    )
                                                    wnd.close()
                                                    break
                                            window["_TABLE_"].update(
                                                values=Assignment.teacher_work(
                                                    Id,
                                                    "",
                                                    "",
                                                    "",
                                                    "",
                                                    "",
                                                    "View",
                                                )[1]
                                            )
                                        continue

                                    elif values[1] == ["Notice"]:
                                        window["_Profile_"].update(
                                            visible=False
                                        )

                                        window["_Admin_"].update(visible=False)
                                        window["_Main_"].update(visible=False)

                                        window["_Data_"].update(visible=False)

                                        window["_Assgn_"].update(visible=False)

                                        window["_Not_"].update(visible=True)
                                        if (
                                            event == "_Notice_"
                                            and values["_Notice_"] != []
                                        ):
                                            rows = Info.Notice()
                                            notice = rows[
                                                (values["_Notice_"])[0]
                                            ][2]
                                            psg.popup_no_buttons(notice)
                                        elif event == "_back_":
                                            window["_Notice_"].update(
                                                values=Info.Notice()
                                            )
                                            continue
                                        elif event == "_new-notice_":
                                            layout_new_notice = [
                                                [
                                                    psg.Input(
                                                        key="_NOTICE-DATE_",
                                                    ),
                                                    psg.CalendarButton(
                                                        "Enter date",
                                                        close_when_date_chosen=True,
                                                        target="_NOTICE-DATE_",
                                                        format="%Y-%m-%d",
                                                        font=(16),
                                                    ),
                                                ],
                                                [
                                                    psg.Text(
                                                        "Enter circular number: ",
                                                        font=(
                                                            "Arial Bold",
                                                            16,
                                                        ),
                                                    ),
                                                    psg.Input(
                                                        expand_x=True,
                                                        font=(16),
                                                    ),
                                                ],
                                                [
                                                    psg.Text(
                                                        "Enter Title: ",
                                                        font=(
                                                            "Arial Bold",
                                                            16,
                                                        ),
                                                    ),
                                                    psg.Input(
                                                        expand_x=True,
                                                        font=(16),
                                                    ),
                                                ],
                                                [
                                                    psg.Text(
                                                        "Browse: ",
                                                        font=(
                                                            "Arial Bold",
                                                            16,
                                                        ),
                                                    ),
                                                    psg.Input(),
                                                    psg.FileBrowse(),
                                                ],
                                                [
                                                    psg.Button(
                                                        "OK",
                                                        font=16,
                                                        auto_size_button=True,
                                                    ),
                                                    psg.Button(
                                                        "Back",
                                                        font=16,
                                                        auto_size_button=True,
                                                    ),
                                                ],
                                            ]

                                            wnd = psg.Window(
                                                "School MyClassroom",
                                                layout_new_notice,
                                                size=(715, 250),
                                                finalize=True,
                                            )
                                            while True:
                                                (
                                                    event,
                                                    values,
                                                ) = wnd.read()
                                                if event == psg.WIN_CLOSED:
                                                    wnd.close()
                                                    break
                                                elif event == "Back":
                                                    wnd.close()
                                                    break
                                                elif "OK" in event:
                                                    circular = open(
                                                        values[2], "r"
                                                    )
                                                    data = circular.read()
                                                    Info.Notice_Add(
                                                        values[0],
                                                        values[1],
                                                        values[
                                                            "_NOTICE-DATE_"
                                                        ],
                                                        data,
                                                    )

                                                    wnd.close()
                                                    break

                                        continue
                                    elif values[1] == ["Student Data"]:
                                        window["_Profile_"].update(
                                            visible=False
                                        )

                                        window["_Admin_"].update(visible=False)
                                        window["_Main_"].update(visible=False)

                                        window["_Assgn_"].update(visible=False)

                                        window["_Data_"].update(visible=True)

                                        window["_Not_"].update(visible=False)
                                        if event == "OK0":
                                            if values[6] != "":
                                                Admin.Viewer(values[6])

                                        continue

                                    else:
                                        window.close()
                                        break
                                break

                            else:
                                print("Password Wrong")
                                wnd.close()
                                break
                        elif Info.Id_Check(User) == None:
                            print("Database Server Error")
                            wnd.close()
                            Info.End()
                            file.close()
                            Editor.End()
                            break
                        else:
                            print("Teacher Id wrong")
                            wnd.close()
                            break
                    break
        break
