# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:41:17 2023

@author: Student
"""
import PySimpleGUI as psg
import Info


def stud_work(SId):
    toprow = ["Date", "Subject", "Link"]
    rows = Info.Assgn_data(SId)
    tbl1 = psg.Table(
        values=rows,
        headings=toprow,
        auto_size_columns=True,
        justification="center",
        key="_TABLE_",
        enable_events=True,
        expand_x=True,
        expand_y=True,
        display_row_numbers=True,
        starting_row_number=1,
        font=("Arial Bold", 20),
    )
    layout = [[tbl1], rows]

    return layout


def teacher_work(TId, Sec, Div, Date, Topic, Link, Mode):
    toprow = ["Date", "Topic", "Link"]
    rows = Info.update_assgn(TId, Sec, Div, Date, Topic, Link, Mode)
    tbl1 = psg.Table(
        values=rows,
        headings=toprow,
        auto_size_columns=True,
        justification="center",
        key="_TABLE_",
        enable_events=True,
        expand_x=True,
        expand_y=True,
        display_row_numbers=True,
        starting_row_number=1,
        font=("Arial Bold", 20),
    )
    layout = [[tbl1], rows]

    return layout
