"""
NOVA IMS
Data Mining
2019/2020
"""

__author__ = "Francisco Neves"
__version__ = "1.0.0"

baseWork_engage=df_engage_outliers.copy().drop(columns=['c_ID'])
Work_engage=df_engage_outliers.copy().drop(columns=['c_ID','Educational_Degree','Living_Area','Children'])

scaler = StandardScaler()

Engage_Normalized = scaler.fit_transform(Work_engage)
Engage_Normalized = pd.DataFrame(Engage_Normalized, columns=Work_engage.columns)

########
#KMeans#
########

Edistortion = []
for n in range(1,21):
    E_elbowkmeans = KMeans(n_clusters=n).fit(Work_engage)
    Edistortion.append(E_elbowkmeans.inertia_)

plt.plot(range(1,21),Edistortion)


E_kmeans = KMeans(n_clusters=3,random_state=0,n_init=10,max_iter=2000).fit(Engage_Normalized)
E_kmeanCluster = pd.DataFrame(E_kmeans.cluster_centers_)
E_kmeanCluster = pd.DataFrame(scaler.inverse_transform(X=E_kmeanCluster), columns = Work_engage.columns)

##############
#Hierarchical#
##############

E_Z = linkage(Engage_Normalized, method='ward')
dendrogram(Z, truncate_mode='lastp',p=10,orientation='top',leaf_rotation=45,leaf_font_size=10,show_contracted=True,show_leaf_counts=True)
plt.show()


E_HClustering = AgglomerativeClustering(n_clusters=3,affinity='euclidean',linkage='ward').fit(Engage_Normalized)

E_HC_labels = pd.DataFrame(E_HClustering.labels_)
E_HC_labels.columns = ['Cluster']

#print(silhouette_score(Engage_Normalized,E_HClustering.labels_,metric='euclidean'))

E_Affinity = pd.DataFrame(pd.concat([pd.DataFrame(Engage_Normalized),E_HC_labels],axis=1),columns=['First_Policy_Year','Salary','Customer_Value','Claims_Rate','Cluster'])

E_to_revert = E_Affinity.groupby(['Cluster'])['First_Policy_Year','Salary','Customer_Value','Claims_Rate'].mean()

E_HierarchicalCluster = pd.DataFrame(scaler.inverse_transform(X=E_to_revert),columns = ['First_Policy_Year','Salary','Customer_Value','Claims_Rate'])

########
#KMODES#
########


Eng_Cat = baseWork_engage[['Educational_Degree','Living_Area','Children']].astype('str')


kmodes = KModes(n_clusters=3, init='random', n_init=50, verbose=1)
kmclusters = kmodes.fit_predict(Eng_Cat)

eng_centroids = pd.DataFrame(kmodes.cluster_centroids_,)

###########
#MEANSHIFT#
###########

my_bandwidth = estimate_bandwidth(Engage_Normalized,quantile=0.2,n_samples=1000)
E_meanS = MeanShift(bandwidth = my_bandwidth,bin_seeding=True).fit(Engage_Normalized)
E_MS_labels = E_meanS.labels_
E_MS_cluster_centers = E_meanS.cluster_centers_
e_label_unique = np.unique(E_MS_labels)
E_MS_n_clusters=len(e_label_unique)

E_MS_Clusters=scaler.inverse_transform(X=E_MS_cluster_centers)

########
#DBSCAN#
########

E_dbscan = DBSCAN(eps=0.5,min_samples=10).fit(Engage_Normalized)
E_dbs_labels = E_dbscan.labels_

E_n_clusters_ = len(set(E_dbs_labels)) - (1 if -1 in E_dbs_labels else 0)
unique_clusters , counts_clusters = np.unique(E_dbscan.labels_, return_counts = True)

E_pcaDBS = PCA(n_components=2).fit(Engage_Normalized)
E_pca_2dDBS = E_pcaDBS.transform(Engage_Normalized)
for i in range(0, pca_2dDBS.shape[0]):
    if E_dbs_labels[i] == 0:
        c1 = plt.scatter(E_pca_2dDBS[i,0],E_pca_2dDBS[i,1],c='r',marker='+')
    elif E_dbs_labels[i] == 1:
        c2 = plt.scatter(E_pca_2dDBS[i,0],E_pca_2dDBS[i,1],c='g',marker='o')
    elif E_dbs_labels[i] == 2:
        c4 = plt.scatter(E_pca_2dDBS[i,0],E_pca_2dDBS[i,1],c='k',marker='v')
    elif E_dbs_labels[i] == 3:
        c5 = plt.scatter(E_pca_2dDBS[i,0],E_pca_2dDBS[i,1],c='y',marker='s')
    elif E_dbs_labels[i] == 4:
        c6 = plt.scatter(E_pca_2dDBS[i,0],E_pca_2dDBS[i,1],c='m',marker='p')
    elif E_dbs_labels[i] == 5:
        c7 = plt.scatter(E_pca_2dDBS[i,0],E_pca_2dDBS[i,1],c='c',marker='H')
    elif E_dbs_labels[i] == -1:
        c3 = plt.scatter(E_pca_2dDBS[i,0],E_pca_2dDBS[i,1],c='b',marker='*')

plt.legend([c1, c2, c3], ['Cluster 1', 'Cluster 2','Noise'])
plt.title('DBSCAN finds N clusters and noise')
plt.show()


#####
#PCA#
#####

from sklearn.decomposition import PCA
pca = PCA(n_components= Work_engage.shape[1])
principalComponents = pca.fit_transform(Engage_Normalized)

E_a = pca.inverse_transform(principalComponents)






####
#EM#
####

gmm = mixture.GaussianMixture(n_components=3,init_params='kmeans',max_iter=1000,n_init=10,verbose=1).fit(Engage_Normalized)

EM_labels_ = gmm.fit_predict(Engage_Normalized)
EM_score_sample=gmm.score_samples(Engage_Normalized)
EM_pred_probabilit=gmm.predict_proba(Engage_Normalized)
EM_Cluster = scaler.inverse_transform(gmm.means_)
