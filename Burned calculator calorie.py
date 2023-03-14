import streamlit as st
import pandas as pd
import numpy as np
import pickle

loaded_model = pickle.load(open('trained_model.sav', 'rb'))


def calories_prediction(input_data):
    input_data = np.asarray(input_data).astype('float').reshape(1, -1)
    try:
        prediction = loaded_model.predict(input_data)
        return prediction
    except:
        return "Invalid input data"


def main():
    st.title('Предсказатель сжигаемых калорий')
    Gender = st.text_input('Ваш пол')
    Age = st.text_input('Ваш возраст')
    Height = st.text_input('Ваш рост')
    Weight = st.text_input('Ваш вес')
    Duration = st.text_input('Длительность выполнения упражнения')
    Heart_Rate = st.text_input('Сердечный ритм')
    Body_Temp = st.text_input('Температура тела')
    calories = []
    if st.button('Узнать количество калорий'):
        calories = calories_prediction([Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp])
    st.success(calories)


if __name__ == '__main__':
    main()
