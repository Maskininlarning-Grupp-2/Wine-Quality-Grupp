from models.preprocessing import X_train, X_test, y_train, y_test
from sklearn.ensemble import RandomForestClassifier
import joblib

# Träna modellen
model = RandomForestClassifier(n_estimators=100, random_state=0)
model.fit(X_train, y_train)

# Kolla score
print(f"Train: {model.score(X_train, y_train):.4f}")
print(f"Test:  {model.score(X_test, y_test):.4f}")

# Spara modellen
joblib.dump(model, "models/random_forest.pkl")
print("Modell sparad!")