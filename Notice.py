# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:28:12 2023

@author: Net
"""
import PySimpleGUI as psg


def Disp(notice):
    """Function to display notices when called by mcb"""
    toprow = ["Date", "Title"]
    rows = []
    for x in notice:
        rows.append([x[0], x[1]])
    tbl1 = psg.Table(
        values=rows,
        headings=toprow,
        auto_size_columns=True,
        justification="center",
        key="_Notice_",
        enable_events=True,
        expand_x=True,
        expand_y=True,
        display_row_numbers=True,
        starting_row_number=1,
        font=("Arial Bold", 20),
    )

    layout = [
        [tbl1],
    ]
    return layout
