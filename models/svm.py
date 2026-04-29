from models.preprocessing import X_train_scaled, X_test_scaled, y_train, y_test
from sklearn.svm import SVC
import joblib

# Träna modellen
model = SVC(kernel="linear", probability=True, random_state=0)
model.fit(X_train_scaled, y_train)

# Kolla score
print(f"Train: {model.score(X_train_scaled, y_train):.4f}")
print(f"Test:  {model.score(X_test_scaled, y_test):.4f}")

# Spara modellen
joblib.dump(model, "models/svm.pkl")