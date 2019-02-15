import pandas as pd

if (__name__ == '__main__'):
    base = pd.read_csv('csv/census.csv');
    previsores = base.iloc[:, 0:14].values
    classe = base.iloc[:, 14];


    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder_previsores = LabelEncoder()
    previsores[:, 1] = labelencoder_previsores.fit_transform(previsores[:,1])
    previsores[:, 3] = labelencoder_previsores.fit_transform(previsores[:, 3])
    previsores[:, 5] = labelencoder_previsores.fit_transform(previsores[:, 5])
    previsores[:, 6] = labelencoder_previsores.fit_transform(previsores[:, 6])
    previsores[:, 7] = labelencoder_previsores.fit_transform(previsores[:, 7])
    previsores[:, 8] = labelencoder_previsores.fit_transform(previsores[:, 8])
    previsores[:, 9] = labelencoder_previsores.fit_transform(previsores[:, 9])
    previsores[:, 13] = labelencoder_previsores.fit_transform(previsores[:, 13])

    onehotencoder = OneHotEncoder(categorical_features=[1,3,5,6,7,8,9,13]);
    previsores = onehotencoder.fit_transform(previsores).toarray()
    print(previsores)