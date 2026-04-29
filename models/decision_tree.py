from sklearn.tree import DecisionTreeClassifier
from models.preprocessing import X_train, X_test, y_train, y_test
import joblib

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

try:
    joblib.dump(clf, "decision_tree.pkl")
    print("Model saved")
except Exception as e:
    print(f"Model could not be saved:\n"
          f"{e}")