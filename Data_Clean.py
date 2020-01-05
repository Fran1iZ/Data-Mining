"""
NOVA IMS
Data Mining
2019/2020
"""

__author__ = "Francisco Neves, Francisco Jorge and Pedro Carmona"
__version__ = "1.0.0"
#Invalid Data
#Some birthdays are after the first policy

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

#some birthdays are after the first policy year
#assumed it was human error

df_engage.drop('Birthday',axis = 1, inplace= True)


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

#sns.boxplot(x=df_engage['Salary'])
# remove above 5022 - 2val

#sns.boxplot(x=df_engage['Customer_Value'])
# remove below -500 and above 1011 - 14 + 3 vals

#sns.boxplot(x=df_engage['Claims_Rate'])
# remove above 1.56 - 4 vals

#tot - 24 values (may have duplicates)

engage_outliersList = df_engage.loc[df_engage['First_Policy_Year']>1999]
"""
print("FPY")
print(df_engage.loc[df_engage['First_Policy_Year']>1999])

print("SAL")
print(df_engage.loc[df_engage['Salary']>5025])

print("CVAL+")
print(df_engage.loc[df_engage['Customer_Value']>2500])

print("CVAL-")
print(df_engage.loc[df_engage['Customer_Value']<-500])

print("CLRAT")
print(df_engage.loc[df_engage['Claims_Rate']>40])
"""

#check with others - temp thus far

#500 > Value > 2500
#Claim_Rate > 40

#engage_outliersList = engage_outliersList.append(df_engage.loc[df_engage['First_Policy_Year']>1999]['c_ID'])

engage_outliersList = engage_outliersList.append(df_engage.loc[df_engage['Salary']>5025])
engage_outliersList = engage_outliersList.append(df_engage.loc[df_engage['Customer_Value']>2500])
engage_outliersList = engage_outliersList.append(df_engage.loc[df_engage['Customer_Value']<-500])
engage_outliersList = engage_outliersList.append(df_engage.loc[df_engage['Claims_Rate']>40])

#print(engage_outliersList.drop_duplicates())
engage_outliersList = engage_outliersList.drop_duplicates()
# after clearing dups - 20 values

df_engage_outliers = df_engage.copy()

df_engage_outliers = df_engage_outliers.loc[~df_engage_outliers['c_ID'].isin(engage_outliersList['c_ID'])]
#print(df_engage_outliers)
#creates copy df without outliers

#lob

#sns.boxplot(x=df_lob['Motor'])
# remove values aboxe 590

#sns.boxplot(x=df_lob['Household'])
# remove above 2000

#sns.boxplot(x=df_lob['Health'])
# remove above 500

#sns.boxplot(x=df_lob['Life'])
# remove above 370

#sns.boxplot(x=df_lob['Work_Compensation'])
# remove above 360


lob_outliersList = df_lob.loc[df_lob['Motor']>590]


lob_outliersList = lob_outliersList.append(df_lob.loc[df_lob['Household']>2000])
lob_outliersList = lob_outliersList.append(df_lob.loc[df_lob['Health']>500])
lob_outliersList = lob_outliersList.append(df_lob.loc[df_lob['Life']>370])
lob_outliersList = lob_outliersList.append(df_lob.loc[df_lob['Work_Compensation']>360])

lob_outliersList = lob_outliersList.drop_duplicates()
df_lob_outliers=df_lob.copy()

df_lob_outliers = df_lob_outliers.loc[~df_lob_outliers['c_ID'].isin(lob_outliersList['c_ID'])]
