# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:01:50 2023

@author: Net
"""

import PySimpleGUI as psg
import Info
import Profile


def Disp(SId, Details):
    Intro = Profile.smallDisp(SId, Details)
    toprow = ["Date", "Day", "Status"]
    January = [
        [
            psg.Table(
                values=Info.Attendance("01", SId),
                headings=toprow,
                auto_size_columns=True,
                justification="center",
                key="_Tbl01_",
                def_col_width=20,
                enable_events=False,
                expand_x=True,
                expand_y=True,
                size=(1350, 100),
                display_row_numbers=False,
                font=("Arial Bold", 20),
            )
        ]
    ]
    February = [
        [
            psg.Table(
                values=Info.Attendance("02", SId),
                headings=toprow,
                auto_size_columns=True,
                justification="center",
                key="_Tbl02_",
                def_col_width=20,
                enable_events=False,
                expand_x=True,
                expand_y=True,
                size=(1350, 100),
                display_row_numbers=False,
                font=("Arial Bold", 20),
            )
        ]
    ]
    March = [
        [
            psg.Table(
                values=Info.Attendance("03", SId),
                headings=toprow,
                auto_size_columns=True,
                justification="center",
                key="_Tbl03_",
                def_col_width=20,
                enable_events=False,
                expand_x=True,
                expand_y=True,
                size=(1350, 100),
                display_row_numbers=False,
                font=("Arial Bold", 20),
            )
        ]
    ]
    April = [
        [
            psg.Table(
                values=Info.Attendance("04", SId),
                headings=toprow,
                auto_size_columns=True,
                justification="center",
                key="_Tbl04_",
                def_col_width=20,
                enable_events=False,
                expand_x=True,
                expand_y=True,
                size=(1350, 100),
                display_row_numbers=False,
                font=("Arial Bold", 20),
            )
        ]
    ]
    May = [
        [
            psg.Table(
                values=Info.Attendance("05", SId),
                headings=toprow,
                auto_size_columns=True,
                justification="center",
                key="_Tbl05_",
                enable_events=False,
                def_col_width=20,
                expand_x=True,
                expand_y=True,
                size=(100, 100),
                display_row_numbers=False,
                font=("Arial Bold", 20),
            )
        ]
    ]
    June = [
        [
            psg.Table(
                values=Info.Attendance("06", SId),
                headings=toprow,
                auto_size_columns=True,
                justification="center",
                key="_Tbl06_",
                def_col_width=20,
                enable_events=False,
                expand_x=True,
                expand_y=True,
                size=(1350, 100),
                display_row_numbers=False,
                font=("Arial Bold", 20),
            )
        ]
    ]
    July = [
        [
            psg.Table(
                values=Info.Attendance("07", SId),
                headings=toprow,
                auto_size_columns=True,
                justification="center",
                key="_Tbl07_",
                def_col_width=20,
                enable_events=False,
                expand_x=True,
                expand_y=True,
                size=(100, 100),
                display_row_numbers=False,
                font=("Arial Bold", 20),
            )
        ]
    ]
    August = [
        [
            psg.Table(
                values=Info.Attendance("08", SId),
                headings=toprow,
                auto_size_columns=True,
                justification="center",
                key="_Tbl08_",
                def_col_width=20,
                enable_events=False,
                expand_x=True,
                expand_y=True,
                size=(1350, 100),
                display_row_numbers=False,
                font=("Arial Bold", 20),
            )
        ]
    ]
    September = [
        [
            psg.Table(
                values=Info.Attendance("09", SId),
                headings=toprow,
                auto_size_columns=True,
                justification="center",
                key="_Tbl09_",
                def_col_width=20,
                enable_events=False,
                expand_x=True,
                expand_y=True,
                size=(1350, 100),
                display_row_numbers=False,
                font=("Arial Bold", 20),
            )
        ]
    ]
    October = [
        [
            psg.Table(
                values=Info.Attendance("10", SId),
                headings=toprow,
                auto_size_columns=True,
                justification="center",
                key="_Tbl10_",
                def_col_width=20,
                enable_events=False,
                expand_x=True,
                expand_y=True,
                size=(1350, 100),
                display_row_numbers=False,
                font=("Arial Bold", 20),
            )
        ]
    ]
    November = [
        [
            psg.Table(
                values=Info.Attendance("11", SId),
                headings=toprow,
                auto_size_columns=True,
                justification="center",
                key="_Tbl11_",
                def_col_width=20,
                enable_events=False,
                expand_x=True,
                expand_y=True,
                size=(1350, 100),
                display_row_numbers=False,
                font=("Arial Bold", 20),
            )
        ]
    ]
    December = [
        [
            psg.Table(
                values=Info.Attendance("12", SId),
                headings=toprow,
                auto_size_columns=True,
                justification="center",
                key="_Tbl12_",
                def_col_width=20,
                enable_events=False,
                expand_x=True,
                expand_y=True,
                size=(1350, 100),
                display_row_numbers=False,
                font=("Arial Bold", 20),
            )
        ]
    ]

    layout = [
        [psg.Text(text=Intro, font=("Arial Bold", 16))],
        [psg.VPush()],
        [
            psg.TabGroup(
                [
                    [
                        psg.Tab("April", April),
                        psg.Tab("May", May),
                        psg.Tab("June", June),
                        psg.Tab("July", July),
                        psg.Tab("August", August),
                        psg.Tab("September", September),
                        psg.Tab("October", October),
                        psg.Tab("November", November),
                        psg.Tab("December", December),
                        psg.Tab("January", January),
                        psg.Tab("February", February),
                        psg.Tab("March", March),
                    ]
                ],
                size=(1000, 800),
            )
        ],
    ]
    return layout
