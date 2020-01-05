"""
NOVA IMS
Data Mining
2019/2020
"""

__author__ = "Francisco Neves, Francisco Jorge and Pedro Carmona"
__version__ = "1.0.0"

# Nulls

df_engage = df_engage.dropna()
df_lob = df_lob.dropna()

""" Tests
print(df_engage.isnull().sum())
print(df_lob.isnull().sum())

print("oi")
print(len(df_lob))
print(len(df_lob.dropna()))
print((len(df_lob)-len(df_lob.dropna()))/len(df_lob)*100)
"""

#engage
#total - 10296
#nulls - 92

#lob
#total - 10296
#nulls - 225

#total - 20592
#tot nulls - 317
#tot cleaned - 1.54%

# Outliers

#engage

#sns.boxplot(x=df_engage['First_Policy_Year'])
# remove values aboxe 1999 - 1 val

#sns.boxplot(x=df_engage['Birthday'])
# remove before 1934 -1val

#sns.boxplot(x=df_engage['Salary'])
# remove above 5022 - 2val

#sns.boxplot(x=df_engage['Customer_Value'])
# remove below -500 and above 1011 - 14 + 96 vals

#sns.boxplot(x=df_engage['Claims_Rate'])
# remove above 1.56 - 15 vals

#tot - 129 values (may have duplicates)

engage_outliersList = df_engage.loc[df_engage['First_Policy_Year']>1999]

print("FPY")
print(df_engage.loc[df_engage['First_Policy_Year']>1999])

print("BIRT")
print(df_engage.loc[df_engage['Birthday']<1934])

print("SAL")
print(df_engage.loc[df_engage['Salary']>5022])

print("CVAL+")
print(df_engage.loc[df_engage['Customer_Value']>1011])

print("CVAL-")
print(df_engage.loc[df_engage['Customer_Value']<-500])

print("CLRAT")
print(df_engage.loc[df_engage['Claims_Rate']>1.56])

#check with others - temp thus far


#engage_outliersList = engage_outliersList.append(df_engage.loc[df_engage['First_Policy_Year']>1999]['c_ID'])
engage_outliersList = engage_outliersList.append(df_engage.loc[df_engage['Birthday']<1934])
engage_outliersList = engage_outliersList.append(df_engage.loc[df_engage['Salary']>5022])
engage_outliersList = engage_outliersList.append(df_engage.loc[df_engage['Customer_Value']>1011])
engage_outliersList = engage_outliersList.append(df_engage.loc[df_engage['Customer_Value']<-500])
engage_outliersList = engage_outliersList.append(df_engage.loc[df_engage['Claims_Rate']>1.56])

print(engage_outliersList.drop_duplicates())
engage_outliersList = engage_outliersList.drop_duplicates()
# after clearing dups - 115 values

df_engage_outliers = df_engage.copy()

df_engage_outliers = df_engage_outliers.loc[~df_engage_outliers['c_ID'].isin(engage_outliersList['c_ID'])]
print(df_engage_outliers)
#creates copy df without outliers
