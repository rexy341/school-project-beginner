# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 23:09:26 2023

@author: Net
"""

import Info
import Profile
import PySimpleGUI as psg


def Disp(Exam, SId, Sec, Sub, Sess, Details):
    Intro = Profile.smallDisp(SId, Details)
    toprow = ["Subject", "Out of", "Passing", "Obtained", "Grade"]
    Exam1 = [
        [psg.Text(text=Intro, font=("Arial Bold", 16))],
        [
            psg.Table(
                values=Info.Marksheet(Exam[0][0], SId, Sec, Sub, Sess),
                headings=toprow,
                auto_size_columns=True,
                justification="center",
                key="_Tbl12_",
                def_col_width=20,
                enable_events=False,
                expand_x=True,
                expand_y=True,
                size=(1000, 100),
                display_row_numbers=False,
                font=("Arial Bold", 20),
            )
        ],
    ]

    Exam2 = [
        [psg.Text(text=Intro, font=("Arial Bold", 16))],
        [
            psg.Table(
                values=Info.Marksheet(Exam[1][0], SId, Sec, Sub, Sess),
                headings=toprow,
                auto_size_columns=True,
                justification="center",
                key="_Tbl12_",
                def_col_width=20,
                enable_events=False,
                expand_x=True,
                expand_y=True,
                size=(1000, 100),
                display_row_numbers=False,
                font=("Arial Bold", 20),
            )
        ],
    ]

    Exam3 = [
        [psg.Text(text=Intro, font=("Arial Bold", 16))],
        [
            psg.Table(
                values=Info.Marksheet(Exam[2][0], SId, Sec, Sub, Sess),
                headings=toprow,
                auto_size_columns=True,
                justification="center",
                key="_Tbl12_",
                def_col_width=20,
                enable_events=False,
                expand_x=True,
                expand_y=True,
                size=(1000, 100),
                display_row_numbers=False,
                font=("Arial Bold", 20),
            )
        ],
    ]

    Exam4 = [
        [psg.Text(text=Intro, font=("Arial Bold", 16))],
        [
            psg.Table(
                values=Info.Marksheet(Exam[3][0], SId, Sec, Sub, Sess),
                headings=toprow,
                auto_size_columns=True,
                justification="center",
                key="_Tbl12_",
                def_col_width=20,
                enable_events=False,
                expand_x=True,
                expand_y=True,
                size=(1000, 100),
                display_row_numbers=False,
                font=("Arial Bold", 20),
            )
        ],
    ]

    Exam5 = [
        [psg.Text(text=Intro, font=("Arial Bold", 16))],
        [
            psg.Table(
                values=Info.Marksheet(Exam[4][0], SId, Sec, Sub, Sess),
                headings=toprow,
                auto_size_columns=True,
                justification="center",
                key="_Tbl12_",
                def_col_width=20,
                enable_events=False,
                expand_x=True,
                expand_y=True,
                size=(1000, 100),
                display_row_numbers=False,
                font=("Arial Bold", 20),
            )
        ],
    ]

    layout = [
        [
            psg.TabGroup(
                [
                    [
                        psg.Tab(Exam[0][0], Exam1),
                        psg.Tab(Exam[1][0], Exam2),
                        psg.Tab(Exam[2][0], Exam3),
                        psg.Tab(Exam[3][0], Exam4),
                        psg.Tab(Exam[4][0], Exam5),
                    ]
                ],
                size=(1000, 1000),
            )
        ]
    ]
    return layout
