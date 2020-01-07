"""
NOVA IMS
Data Mining
2019/2020

Order of running
(1) - Pre-Processing.py
(2) - Data_Clean.py
(3) - Either Lob.py or Enga.py for their respective clusters
(4) - Run Cross.py only after running Enga.py
"""
__author__ = "Francisco Neves, Francisco Jorge and Pedro Carmona"
__version__ = "1.0.0"

#imports

import sqlite3
import pandas as pd
import numpy as np
import sklearn
from sklearn import preprocessing
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import plotly as py
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode
import scipy
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
import sklearn.metrics as sm
from sklearn.decomposition import PCA
from kmodes import kmodes
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_samples, silhouette_score
from kmodes.kmodes import KModes
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn import mixture
import os


#get base path to work with all pc's
base_path = os.getcwd()
my_path = base_path + '\insurance.db'
conn = sqlite3.connect(my_path)

query_lob = 'SELECT * FROM LOB'
query_engage = 'SELECT * FROM Engage'

df_lob = pd.read_sql_query(query_lob, conn)
df_engage = pd.read_sql_query(query_engage, conn)


#Rename columns for easier handling
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

#Clears Extra Index Column
df_engage.drop(columns=['index'],inplace=True)
df_lob.drop(columns=['index'],inplace=True)

#Clean Educational Degree -> Convert previous string into a new integer for better analysis
df_engage.loc[df_engage['Educational_Degree'] == '1 - Basic', 'Educational_Degree'] = int('1')
df_engage.loc[df_engage['Educational_Degree'] == '2 - High School', 'Educational_Degree'] = int('2')
df_engage.loc[df_engage['Educational_Degree'] == '3 - BSc/MSc', 'Educational_Degree'] = int('3')
df_engage.loc[df_engage['Educational_Degree'] == '4 - PhD', 'Educational_Degree'] = int('4')
