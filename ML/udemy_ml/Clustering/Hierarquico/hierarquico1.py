import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
import numpy as np
from sklearn.preprocessing import StandardScaler

x = [20, 27, 21, 37, 46, 53, 55, 47, 52, 32, 39, 41, 39, 48, 48]
y = [1000, 1200, 2900, 1850, 900, 950, 2000, 2100, 3000, 5900, 4100, 5100, 7000, 5000, 6500]

# plt.scatter(x, y)

base = np.array([[20, 1000], [27, 1200], [21, 2900], [37, 1850], [46, 900],
                 [53, 950], [55, 2000], [47, 2100], [52, 3000], [32, 5900],
                 [39, 4100], [41, 5100], [39, 7000], [48, 5000], [48, 6500]])

scaler = StandardScaler()
base = scaler.fit_transform(base)

# dendrograma = dendrogram(linkage(base, method='ward'))

# plt.title('Dendrograma')
# plt.xlabel('Pessoas')
# plt.ylabel('Distancia Euclidiana')

# Utilizar 3 clusters

hc = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
previsores = hc.fit_predict(base)

plt.scatter(base[previsores == 0, 0], base[previsores == 0, 1], s=100, c='red', label='Cluster1')
plt.scatter(base[previsores == 1, 0], base[previsores == 1, 1], s=100, c='blue', label='Cluster2')
plt.scatter(base[previsores == 2, 0], base[previsores == 2, 1], s=100, c='green', label='Cluster3')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.legend()

plt.show()
