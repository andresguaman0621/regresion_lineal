# Regresión Lineal Simple, usando Smartphone Sales vs Consumer Spending

# Importar bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Importar el dataset
dataset = pd.read_csv('Global_Tech_Gadget_Consumption.csv')

# Seleccionar las columnas relevantes
X = dataset[['Smartphone Sales (Millions)']].values  # Variable independiente
y = dataset['Average Consumer Spending on Gadgets ($)'].values  # Variable dependiente

# Dividir el dataset en conjunto de entrenamiento y prueba (2/3 entrenamiento, 1/3 prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

# Entrenar el modelo de regresión lineal
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predecir los resultados para el conjunto de prueba
y_pred = regressor.predict(X_test)

# # Visualizar los resultados del conjunto de entrenamiento
# plt.scatter(X_train, y_train, color='red')  # Puntos reales
# plt.plot(X_train, regressor.predict(X_train), color='blue')  # Línea de regresión
# plt.title('Gasto de Clientes vs Ventas de Smartphones (Set Entrenamiento)')
# plt.xlabel('Venta de Smartphones (Millions)')
# plt.ylabel('Gasto Promedio de Clientes en Gadgets ($)')
# plt.show()

# # Visualizar los resultados del conjunto de prueba
# plt.scatter(X_test, y_test, color='red')  # Puntos reales del test
# plt.plot(X_train, regressor.predict(X_train), color='blue')  # Mismo modelo entrenado
# plt.title('Gasto de Clientes vs Ventas de Smartphones (Set de Prueba)')
# plt.xlabel('Venta de Smartphones (Millions)')
# plt.ylabel('Gasto Promedio de Clientes en Gadgets ($)')
# plt.show()

# Crear la figura y los subgráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Visualizar los resultados del conjunto de entrenamiento en el primer subgráfico
ax1.scatter(X_train, y_train, color='red')  # Puntos reales
ax1.plot(X_train, regressor.predict(X_train), color='blue')  # Línea de regresión
ax1.set_title('Gasto de Clientes vs Ventas de Smartphones (Set Entrenamiento)')
ax1.set_xlabel('Venta de Smartphones (Millions)')
ax1.set_ylabel('Gasto Promedio de Clientes en Gadgets ($)')

# Visualizar los resultados del conjunto de prueba en el segundo subgráfico
ax2.scatter(X_test, y_test, color='red')  # Puntos reales del test
ax2.plot(X_train, regressor.predict(X_train), color='blue')  # Mismo modelo entrenado
ax2.set_title('Gasto de Clientes vs Ventas de Smartphones (Set de Prueba)')
ax2.set_xlabel('Venta de Smartphones (Millions)')
ax2.set_ylabel('Gasto Promedio de Clientes en Gadgets ($)')

# Mostrar las gráficas
plt.tight_layout()  
plt.show()
