# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:09:36 2023

@author: Data
"""

import PySimpleGUI as psg


def DispProfile(SId, Pass, Data):
    """Function to display Data profile"""
    Intro = (
        "\nName: "
        + (Data[1] + " " + Data[2])
        + "\n"
        + "Roll No.: "
        + str(Data[8])
        + "\n"
        + "Class: "
        + str(Data[6])
        + Data[7]
        + "\n"
        + "Password: "
        + "*" * (len(str(Pass)))
        + "\n"
        + "House: "
        + Data[11]
        + "\n"
    )

    Subj = ""
    for x in Data[9]:
        if x != None:
            Subj += x + "\n"

    Sub = "Subjects:\n\n" + Subj

    Personal_Data = (
        "Mother's Name: "
        + Data[5]
        + " "
        + Data[2]
        + "\n"
        + "Father's Name: "
        + Data[4]
        + " "
        + Data[2]
        + "\n"
        + "Phone Number: "
        + Data[14]
        + "\n\n"
        + "Address:\n"
        + Data[15]
        + "\n"
        + Data[16]
        + "\n"
        + Data[17]
        + "\n"
        + Data[18]
        + "\n"
        + Data[19]
        + "\n"
    )
    Profile_pg = [
        [
            psg.Column(
                [
                    [
                        psg.Text(
                            text=Intro,
                            font=("Arial Bold", 20),
                            justification="left",
                        )
                    ],
                    [psg.VPush()],
                    [
                        psg.Text(
                            text=Sub,
                            font=("Arial Bold", 20),
                            justification="left",
                        )
                    ],
                ],
            ),
            psg.Push(),
            psg.Column(
                [
                    [
                        psg.Image(
                            filename="Profile.png", size=(400, 250)
                        )
                    ],
                    [
                        psg.Text(
                            text=Personal_Data,
                            font=("Arial Bold", 20),
                            justification="left",
                        )
                    ],
                ],
            ),
        ]
    ]

    return Profile_pg


def DispProfile_T(TId, Pass, Data):
    """Function to display Data profile"""
    Intro = (
        "\nName: "
        + (Data[1] + " " + Data[2])
        + "\n"
        + "Teacher Id.: "
        + str(Data[0])
        + "\n"
        + "Class: "
        + Data[4]
        + "\n"
        + "Password: "
        + "*" * (len(str(Pass)))
        + "\n"
        + "Subject: "
        + Data[5]
        + "\n"
    )

    Personal_Data = (
        "Date of Birth:"
        + str(Data[6])
        + "\n"
        + "House: "
        + Data[7]
        + "\n"
        + "Gender: "
        + Data[8]
        + "\n"
        + "Phone Number: "
        + Data[10]
        + "\n"
        + "\nAddress:\n"
        + Data[11]
        + "\n"
        + Data[12]
        + "\n"
        + Data[13]
        + "\n"
        + Data[14]
        + "\n"
        + Data[15]
    )
    Profile_pg = [
        [
            psg.Column(
                [
                    [
                        psg.Text(
                            text=Intro,
                            font=("Arial Bold", 20),
                            justification="left",
                        )
                    ],
                    [
                        psg.Text(
                            text=Personal_Data,
                            font=("Arial Bold", 20),
                            justification="left",
                        )
                    ],
                ],
            ),
            psg.Push(),
            psg.Column(
                [
                    [
                        psg.Image(
                            filename="Profile.png", size=(400, 250)
                        )
                    ]
                ],
            ),
        ]
    ]
    return Profile_pg


def smallDisp(SId, Data):
    """Function to display Data profile"""
    Intro = (
        "\nName: "
        + (Data[1] + " " + Data[2])
        + "\n"
        + "Roll No.: "
        + str(Data[8])
        + "\n"
        + "Class: "
        + str(Data[6])
        + Data[7]
        + "\n"
        + "Student Id: "
        + SId
    )
    return Intro
