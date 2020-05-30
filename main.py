# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:53:25 2020

@author: ELCOT
"""
import sqlite3
import pandas as pd

# read the file in to a varaible 
dp="C:/Users/ELCOT/Documents/STUD DET.xlsx"
df=pd.read_excel(dp)

#db connection
db_name="school.db"
conn = sqlite3.connect(db_name)
cur=conn.cursor()

# push into database
df.to_sql(name="students_detail",con=conn,if_exists="append")

#read and dislay data
cur.execute('select * from students_detail')

for row in cur:
    print(row)
    
print("------printing student master---------")

cur.execute('select * from students_master')

for row1 in cur:
    print(row1)

cur.close()