import pandas as pd

base = pd.read_csv('../csv/plano-saude.csv')

X = base.iloc[:, 0].values
y = base.iloc[:, 1].values

import numpy as np

correlacao = np.corrcoef(X, y)

X = X.reshape(-1, 1);

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, y)

# b0
print(regressor.intercept_)

# b1
print(regressor.coef_)

import matplotlib.pyplot as plt
plt.scatter(X, y)
plt.plot(X, regressor.predict(X), color='red')
plt.title('Regressao linear simples')
plt.xlabel('Idade')
plt.ylabel('Custo')

# previsao1 = regressor.predict(40)
# previsao2 = regressor.intercept_ + regressor.coef_ * 40

score = regressor.score(X, y)
print(score)

# plt.show()

from yellowbrick.regressor import ResidualsPlot
visualizador = ResidualsPlot(regressor)
visualizador.fit(X, y)
visualizador.poof()