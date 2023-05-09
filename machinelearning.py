import numpy as np
import pandas as pd
import sklearn.metrics as sm
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, PolynomialFeatures, StandardScaler
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv("test.csv")
del (df["Unnamed: 0"])
df["test"] = 0
label_encoder = LabelEncoder()
df["test"] = label_encoder.fit_transform(df["titre"])
df.to_csv("palala.csv")
liste = df["test"].unique()
liste_sort = np.sort(liste)
df_sort = df[df["prix_moyenne"] != 0]
df_sort = df_sort[df_sort["adresse"] != 0]
df_sort["Ville_tsf"] = label_encoder.fit_transform(df_sort["Ville"])

df_sort = df_sort.dropna()
X = df_sort[["note",
             "Free High Speed Internet (WiFi)",
             "Bar / lounge",
             "Fitness Center with Gym / Workout Room",
             "Parking",
             "Free breakfast",
             "Restaurant",
             "Pool",
             "Ville_tsf"]]

Y = df_sort["prix_moyenne"]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
poly = PolynomialFeatures(degree=2)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)

regressor = LinearRegression()
regressor.fit(X_poly_train, y_train)
y_pred = regressor.predict(X_poly_test)
a = r2_score(y_test, y_pred)
df_sort.to_csv("fin.csv")
liste_ville = df_sort["Ville"].unique()


print("Résultat avec Regression polynomiale")
print("MSE = ", round(sm.mean_squared_error(y_test, y_pred), 2))
print("MAE = ", round(sm.mean_absolute_error(y_test, y_pred), 2))

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
y_pred = ridge.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)


print("Résultat avec Ridge")
print("MSE: ", mse)
print("MAE: ", mae)

lasso = Lasso(alpha=1.0)
lasso.fit(X_train, y_train)
y_pred = lasso.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("Résultat avec Lasso")
print("MSE: ", mse)
print("MAE: ", mae)
tree = DecisionTreeRegressor(max_depth=5, random_state=42)
tree.fit(X_train, y_train)
y_pred = tree.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("Résultat avec DecisionTreeRegressor")
print("MSE: ", mse)
print("MAE: ", mae)
# regression polynomiale / ridge / Lasso / DecisionTreeRegressor / RandomForestRegressor
rf = RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("Résultat avec RandomForestRegressor")
print("MSE: ", mse)
print("MAE: ", mae)
