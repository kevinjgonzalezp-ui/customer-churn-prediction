# 📊 Predicción de Abandono de Clientes (Customer Churn)

## 📌 Descripción del Proyecto

Este proyecto se centra en la predicción de abandono de clientes utilizando técnicas de Machine Learning.

El churn ocurre cuando un cliente deja de utilizar los servicios de una empresa. Detectar clientes con riesgo de abandono puede ayudar a las empresas a mejorar sus estrategias de retención y reducir pérdidas económicas.

En este proyecto se aplicó un flujo completo de Machine Learning que incluye:

- Limpieza de datos
- Feature Engineering
- Escalado de variables
- Balanceo de clases
- Entrenamiento de modelos
- Hyperparameter Tuning
- Evaluación de modelos


# 📂 Dataset

Dataset utilizado:

`WA_Fn-UseC_-Telco-Customer-Churn.csv`

El dataset contiene información de clientes de telecomunicaciones, incluyendo:

- Información demográfica
- Servicios contratados
- Facturación
- Tipo de contrato
- Estado de abandono (Churn)



# 🎯 Objetivo

El objetivo principal del proyecto es construir un modelo de Machine Learning capaz de identificar clientes con alto riesgo de abandono.

Se dio especial importancia a la métrica Recall, ya que detectar correctamente clientes con churn es más importante que obtener únicamente una alta precisión global.



# 🧹 Limpieza de Datos

Se realizaron los siguientes procesos de limpieza:

- Verificación de valores nulos
- Verificación de duplicados
- Conversión de `TotalCharges` de tipo object a numérico
- Eliminación de valores nulos
- Eliminación de la columna `customerID`



# ⚙️ Feature Engineering

Se realizaron distintas transformaciones para preparar los datos para los modelos de Machine Learning:

- Conversión binaria (`Yes/No → 1/0`)
- Codificación de género
- One-Hot Encoding mediante `pd.get_dummies()`
- Separación entre variables predictoras (`X`) y variable objetivo (`y`)

Después del preprocesamiento, el dataset quedó compuesto por 30 variables predictoras.



# ✂️ Train-Test Split

El dataset fue dividido en:

- 80% datos de entrenamiento
- 20% datos de prueba

```python
train_test_split(test_size=0.2, random_state=42)
```

# 📏 Escalado de Variables

Se aplicó StandardScaler() para normalizar las variables antes del entrenamiento de los modelos.

## 🤖 Modelos Base

- KNN
- Logistic Regression

## 🌲 Modelos Comparados

Se entrenaron y compararon los siguientes modelos:

- Decision Tree
- Bagging Classifier
- Random Forest
- AdaBoost
- Gradient Boosting


# ⚖️ Balanceo de Clases

El dataset presentaba un problema de desbalanceo de clases.

Para solucionarlo, se aplicó la técnica SMOTE (Synthetic Minority Oversampling Technique), generando datos sintéticos para equilibrar ambas clases en el conjunto de entrenamiento.

SMOTE(random_state=42)

Hyperparameter Tuning

Se aplicaron técnicas de optimización de hiperparámetros para mejorar el rendimiento de los modelos:

RandomizedSearchCV
GridSearchCV

El tuning se aplicó principalmente sobre:

- Logistic Regression
- AdaBoost

# 📈 Métricas de Evaluación

Los modelos fueron evaluados utilizando las siguientes métricas:

- Accuracy
- Precision
- Recall
- F1-Score

La métrica principal seleccionada fue Recall, ya que el objetivo del proyecto es detectar la mayor cantidad posible de clientes con riesgo de abandono.

# 🏆 Modelo Final

Tras comparar múltiples algoritmos y aplicar Hyperparameter Tuning, se seleccionó Logistic Regression entrenado con SMOTE como modelo final del proyecto.

Resultados Finales
Métrica	Valor
Accuracy	0.74
Recall	0.80
F1-Score	0.62

El modelo logró un buen equilibrio entre Recall y estabilidad general del modelo.

# 🛠️ Tecnologías Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- Imbalanced-Learn
- Jupyter Notebook
- VS Code

# 🚀 Trabajo Futuro

Posibles mejoras futuras del proyecto:

- Probar modelos ensemble más avanzados
- Utilizar visualizaciones con matriz de confusión
- Aplicar técnicas de selección de variables
- Utilizar datasets más grandes
- Realizar visualizaciones EDA más avanzadas

# 👨‍💻 Autor

Kevin Gonzalez

Proyecto de Machine Learning — Data Analytics Bootcamp