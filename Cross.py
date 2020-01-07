# -*- coding: utf-8 -*-
"""
NOVA IMS
Data Mining
2019/2020
"""

__author__ = "Francisco Neves"
__version__ = "1.0.0"

crossdf = pd.DataFrame(columns=["c_id"])
crossdf.c_id = df_engage_outliers.c_ID

crossdf['kmode_cluster']=kmodcl
###kmode labels

#kmeans label kmcl
crossdf = pd.concat([crossdf,kmcl],axis=1)
crossdf.columns = ["c_id","kmode_cluster","kmeans_cluster"]



# kmeans
crossdf['kmeans_cluster'].replace(to_replace=0, value='Low Value', inplace=True)
crossdf['kmeans_cluster'].replace(to_replace=1, value='Wealthier', inplace=True)
crossdf['kmeans_cluster'].replace(to_replace=2, value='Highly Valuable', inplace=True)

# kmodes
crossdf['kmode_cluster'].replace(to_replace=0, value='La4MediumEducationNoChildren', inplace=True)
crossdf['kmode_cluster'].replace(to_replace=1, value='La1HighEducationChildren', inplace=True)
crossdf['kmode_cluster'].replace(to_replace=2, value='La4MediumEducationChildren', inplace=True)



print(crossdf.groupby(['kmeans_cluster']).size())
print(crossdf.groupby(['kmodes_cluster']).size())
print(crossdf.groupby(['kmeans_cluster','kmode_cluster']).size())
