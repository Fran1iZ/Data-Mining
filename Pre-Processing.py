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
import seaborn as sns
import os


#get base path to work with all pc's
base_path = os.getcwd()
my_path = base_path + '\insurance.db'
conn = sqlite3.connect(my_path)

query_lob = 'SELECT * FROM LOB'
query_engage = 'SELECT * FROM Engage'

df_lob = pd.read_sql_query(query_lob, conn)
df_engage = pd.read_sql_query(query_engage, conn)


#Rename columns

df_lob.rename(index = str, columns = {'Customer Identity':'c_ID',
                                    'Premiums in LOB: Motor':'Motor',
                                    'Premiums in LOB: Household' : 'Household',
                                    'Premiums in LOB: Health':'Health',
                                    'Premiums in LOB:  Life':'Life',
                                    'Premiums in LOB: Work Compensations':'Work_Compensation'},inplace = True )


df_engage.rename(index = str, columns = {'Customer Identity':'c_ID',
                                      'First Policy´s Year':'First_Policy_Year',
                                      'Brithday Year':'Birthday',
                                      'Educational Degree':'Educational_Degree',
                                      'Gross Monthly Salary':'Salary',
                                      'Geographic Living Area':'Living_Area',
                                      'Has Children (Y=1)':'Children',
                                      'Customer Monetary Value':'Customer_Value',
                                      'Claims Rate':'Claims_Rate'},inplace = True )


df_engage.loc[df_engage['Educational_Degree'] == '1 - Basic', 'Educational_Degree'] = int('1')
df_engage.loc[df_engage['Educational_Degree'] == '2 - High School', 'Educational_Degree'] = int('2')
df_engage.loc[df_engage['Educational_Degree'] == '3 - BSc/MSc', 'Educational_Degree'] = int('3')
df_engage.loc[df_engage['Educational_Degree'] == '4 - PhD', 'Educational_Degree'] = int('4')
