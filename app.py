import streamlit as st

st.title("Customer Churn Prediction")

st.write("Proyecto de Machine Learning para predicción de abandono de clientes.")

st.header("Objetivo del Proyecto")

st.write("""
El objetivo de este proyecto es predecir qué clientes tienen mayor riesgo de abandonar la compañía utilizando técnicas de Machine Learning.
""")

st.header("Limpieza y Preparación de Datos")

st.write("""
- Se limpiaron valores nulos y duplicados.
- Se transformaron variables categóricas a formato numérico.
- Se aplicó One-Hot Encoding.
- Se utilizó StandardScaler para el escalado de variables.
- Se aplicó SMOTE para balancear las clases.
""")


st.header("Modelos Utilizados")

st.write("""
- Logistic Regression
- Decision Tree
- Random Forest
- AdaBoost
- Gradient Boosting
""")

st.header("Resultados del Modelo Final")

st.write("""
El modelo seleccionado fue Logistic Regression con SMOTE y Hyperparameter Tuning.
""")

st.metric("Recall", "0.80")
st.metric("Accuracy", "0.74")
st.metric("F1-Score", "0.62")

st.header("Conclusión")

st.success("""
Logistic Regression fue el modelo seleccionado por lograr el mejor equilibrio entre Recall y estabilidad general del modelo.
""")

st.sidebar.title("Customer Churn Project")
st.sidebar.write("Ironhack Data Analytics Bootcamp")