# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:47:42 2023

@author: Student
"""
import sys
import Info
from datetime import datetime

try:
    import PySimpleGUI as psg
except:
    print(
        "Your system does not possess the requirements for running this application"
    )


def End():
    try:
        sys.exit()
    except:
        sys.exit()


def Menu(User):
    if User == "Student":
        Menu = [
            "Profile",
            "Assignments",
            "Notice",
            "Attendence",
            "Marksheet",
            "About Us",
        ]
    elif User == "Teacher":
        Menu = [
            "Profile",
            "Student Data",
            "Admin Access",
            "Assignments",
            "Notice",
        ]
    return Menu


def UpdatePass(Id, Pass, User):
    Pass_check = psg.popup_get_text(
        "Enter your previous password: ",
        title="Password",
        password_char="*",
        font=(16),
    )
    if Pass_check == Pass:
        Pass = psg.popup_get_text(
            "Enter your new password: ",
            title="Password",
            password_char="*",
            font=(16),
        )
        Info.Pwd_Updater(Id, Pass, User)
    elif Pass_check != Pass and Pass_check != None:
        psg.PopupQuickMessage("Wrong Password")

    else:
        pass
    return None


def validate(date_text):
    try:
        formated = "%Y-%m-%d"
        datetime.strptime(date_text, formated)
    except ValueError:
        return None
    else:
        return -1


def Grader(records):
    obt_mks = records[3]
    tot_mks = records[1]
    percent = (obt_mks * 100) // tot_mks

    if percent >= 95:
        return "A2"
    elif percent >= 90 and percent < 95:
        return "A1"
    elif percent >= 85 and percent < 90:
        return "B2"
    elif percent >= 80 and percent < 85:
        return "B1"
    elif percent >= 70 and percent < 80:
        return "C2"
    elif percent >= 60 and percent < 70:
        return "C1"
    elif percent >= 50 and percent < 60:
        return "D"
    elif percent <= 33:
        return "F"
