from sklearn.linear_model import LogisticRegression
from models.preprocessing import X_train_scaled, X_test_scaled, y_train, y_test, X_train
import joblib


modelTraining = LogisticRegression(max_iter=1000)
modelTraining.fit(X_train,y_train)

print(f"Training accuracy: {modelTraining.score(X_train_scaled, y_train)}")
print(f"Test accuracy: {modelTraining.score(X_test_scaled, y_test)}")


joblib.dump(modelTraining, "logistic_regression.pkl") #skickar det till logistic regression.pkl


