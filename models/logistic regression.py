import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

df = pd.read_csv("dataset/WineQT.csv")

X = df.drop("quality",axis=1)
y = df["quality"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
scaler = StandardScaler() 
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


modelTraining = LogisticRegression(max_iter=1000)
modelTraining.fit(X_train,y_train)

print(f"Training accuracy: {modelTraining.score(X_train, y_train)}")
print(f"Test accuracy: {modelTraining.score(X_test, y_test)}")

try:
    joblib.dump(modelTraining, "logistic_regression.pkl") #skickar det till logistic regression.pkl
    joblib.dump(scaler,"scaler.pkl")
    print("Results was successful saved in files")
except Exception as e:
    print("Error while saving files")

