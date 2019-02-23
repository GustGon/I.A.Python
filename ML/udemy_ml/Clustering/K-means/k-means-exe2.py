import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

x, y = make_blobs(n_samples=200, centers=4)
plt.scatter(x[:, 0], x[:, 1])

kmeans = KMeans(n_clusters=4)
kmeans.fit(x)

previsoes = kmeans.predict(x)
plt.scatter(x[:, 0], x[:, 1], c=previsoes)

plt.show();