# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:22:42 2024

@author: Student
"""
import pickle

file = open(r"Password_data.dat", "wb")

Data = {
    "Sql_data":
        {
            "host": "localhost",
            "user": "practical",
            "password": "15628356@SQL",
            "database": "Schooldb",
        }
    ,
    "Admin_Student": "BBps_Student909",
    "Admin_Staff": "BBps_Staff110",
}

pickle.dump(Data, file)

file.close()
