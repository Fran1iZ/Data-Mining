"""
NOVA IMS
Data Mining
2019/2020
"""

__author__ = "Francisco Neves"
__version__ = "1.0.0"

work_lob=df_lob_outliers.copy().drop(columns=['c_ID'])

scaler = StandardScaler()

Lob_Normalized = scaler.fit_transform(work_lob)
Lob_Normalized = pd.DataFrame(Lob_Normalized, columns=work_lob.columns)

                                #########
                                #K-Means#
                                #########

#elbow method
Ldistortion = []
for n in range(1,21):
    elbow_kmeans = KMeans(n_clusters=n).fit(Lob_Normalized)
    Ldistortion.append(elbow_kmeans.inertia_)

plt.plot(range(1,21),Ldistortion)
#3 clusters

kmeans = KMeans(n_clusters=3,random_state=0,n_init=10,max_iter=2000).fit(Lob_Normalized)
kmeanCluster = pd.DataFrame(kmeans.cluster_centers_)
kmeanCluster = pd.DataFrame(scaler.inverse_transform(X=kmeanCluster), columns = work_lob.columns)

#print(silhouette_score(Lob_Normalized,kmeans.labels_,metric='euclidean'))

                            ##############
                            #Hierarchical#
                            ##############


Z = linkage(Lob_Normalized, method='ward')
dendrogram(Z, truncate_mode='lastp',p=10,orientation='top',leaf_rotation=45,
           leaf_font_size=10,show_contracted=True,show_leaf_counts=True)
plt.show()


HClustering = AgglomerativeClustering(n_clusters=3,affinity='euclidean',linkage='ward').fit(Lob_Normalized)
#print(HClustering.labels_)

HC_labels = pd.DataFrame(HClustering.labels_)
HC_labels.columns = ['Cluster']
#print(HC_labels)


#print(silhouette_score(Lob_Normalized,HClustering.labels_,metric='euclidean'))

Affinity = pd.DataFrame(pd.concat([pd.DataFrame(Lob_Normalized),HC_labels],axis=1),
                        columns=['Motor','Household','Health','Life','Work_Compensation','Cluster'])

to_revert = Affinity.groupby(['Cluster'])['Motor','Household','Health','Life','Work_Compensation'].mean()

HierarchicalCluster = pd.DataFrame(scaler.inverse_transform(X=to_revert),
                                   columns = ['Motor','Household','Health','Life','Work_Compensation'])

#print(HierarchicalCluster)

###########
#MeanShift#
###########

my_bandwidth = estimate_bandwidth(Lob_Normalized,quantile=0.2,n_samples=1000)
meanS = MeanShift(bandwidth = my_bandwidth,bin_seeding=True)
meanS.fit(Lob_Normalized)
MS_labels = meanS.labels_
MS_cluster_centers = meanS.cluster_centers_
unique_MS_labels = np.unique(MS_labels)
MS_n_clusters=len(unique_MS_labels)

MS_Clusters = scaler.inverse_transform(X=MS_cluster_centers)

pca = PCA(n_components=2).fit(Lob_Normalized)
pca_2d=pca.transform(Lob_Normalized)
for p in range(0,pca_2d.shape[0]):
    if MS_labels[p] == 0:
        c1 = plt.scatter(pca_2d[p,0],pca_2d[p,1], c='r', marker='+')
    if MS_labels[p] == 1:
        c2 = plt.scatter(pca_2d[p,0],pca_2d[p,1], c='g', marker='*')
    if MS_labels[p] == 2:
        c3 = plt.scatter(pca_2d[p,0],pca_2d[p,1], c='b', marker='H')

plt.legend([c1,c2,c3], ['C1','C2','C3'])
plt.title('MS')
plt.show()


########
#DBSCAN#
########


dbscan = DBSCAN(eps=0.5,min_samples=10).fit(Lob_Normalized)
dbslabels = dbscan.labels_

dbsn_clusters_ = len(set(dbslabels)) - (1 if -1 in dbslabels else 0)
unique_clusters , counts_clusters = np.unique(dbscan.labels_, return_counts = True)


"""
PCA
"""
