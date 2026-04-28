import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


df= pd.read_csv('dataset/WineQT.csv')

X= df.drop(['quality', 'Id'], axis=1)
y=df.quality


X_train, X_test, y_train, y_test= train_test_split(X, y, stratify=y, random_state=0)

X_train_capped = X_train.copy()
X_test_capped = X_test.copy()

cols= X_train.columns

for col in cols:
    Q1 = X_train[col].quantile(0.25)
    Q3 = X_train[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    X_train_capped[col] = X_train_capped[col].clip(lower, upper)
    X_test_capped[col] = X_test_capped[col].clip(lower, upper)

scaler= StandardScaler()

X_train_scaled= scaler.fit_transform(X_train)
X_test_scaled= scaler.transform(X_test)

X_train_clean= scaler.fit_transform(X_train_capped)
X_test_clean= scaler.transform(X_test_capped)


#Att importera:

# from models.preprocessing import X_train, y_train, X_test, y_test, X_train_scaled, X_test_scaled, X_train_clean, X_test_clean