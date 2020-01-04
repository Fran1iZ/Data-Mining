#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
NOVA IMS
Data Mining
2019/2020
"""
__author__ = "Francisco Neves, Francisco Jorge and Pedro Carmona"
__version__ = "1.0.0"

#imports

import sqlite3
import pandas as pd
import numpy as np
import os

base_path = os.getcwd()
my_path = base_path + '\insurance.db'
conn = sqlite3.connect(my_path)

query_lob = 'SELECT * FROM LOB'
query_engage = 'SELECT * FROM Engage'

df_lob = pd.read_sql_query(query_lob, conn)
df_engage = pd.read_sql_query(query_engage, conn)
