import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time


st.title('Titanic data Analysis')

url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
data = pd.read_csv(url)
# Checking the data Set
col1,col2,col3 = st.columns(3)

def raw_data():
    if st.sidebar.checkbox('Task'):
        st.write('Task To be done')
        st.header('Data Preprocessing')
        st.write(
            '''
            1. Handling Missing Values \n
            2. Feature Engineering
        '''
        )
        st.subheader('Data Visualization')
        st.write(
            '''
            1. Survival Rate by Gender \n
            2. Survival Rate by Passenger Class \n
            3. Age Distribution of Passengers \n
            4. Age Distribution by Survival Status

        '''
        )
    if st.sidebar.checkbox('Show Titanic Data'):
        with st.spinner("Please wait..."):
            time.sleep(5)
        st.subheader('Data')
        st.write(data.head(5))

    elif st.sidebar.checkbox('Show Missing Data'):
        with st.spinner("Please wait..."):
            time.sleep(5)
        st.subheader('Data')
        st.write(data.isnull().sum())

    elif st.sidebar.checkbox('Description'):
        with st.spinner("Please wait..."):
            time.sleep(5)
        st.subheader('Data')
        st.write(data.describe())
raw_data()

# Fixing missing values

def fixing_missing_value():
    if st.sidebar.checkbox('Show Clean Data'):

        with st.spinner("Please wait..."):
            time.sleep(5)
        st.subheader('Clean Data ')
        # age
        data['Age'].fillna(data['Age'].median(), inplace=True)

        # embarked
        data['Embarked'].fillna(data['Embarked'].mode()[0],inplace=True)

        # Cabin
        data.drop('Cabin', axis=1,inplace=True)
        return st.write(data.isnull().sum())

fixing_missing_value()

def featureEngeering():
    st.sidebar.header('Feature Engineering')
    if st.sidebar.checkbox('New Columns'):
        with st.spinner("Please wait..."):
            time.sleep(5)
        st.subheader('Clean Data ')
        # Calculate the size of each passenger's family by summing their siblings/spouses and parents/children, and adding one for themselves
        data['FamilySize'] = data['SibSp'] + data['Parch'] + 1

        # Create a new binary feature indicating whether a passenger is traveling alone or with family
        data['IsAlone'] = data['FamilySize'].apply(lambda x: 1 if x == 1 else 0)
        return st.write(data.columns[[-1,-2]])
featureEngeering()

def  Visualize_data():
    st.sidebar.header('Visualization')
    if st.sidebar.checkbox("Survival rate by gender"):        
        pclass_survival = data.groupby('Pclass')['Survived'].mean().reset_index()
        fig_pclass_survival = px.bar(pclass_survival, x='Pclass', y='Survived', title='Survival Rate by Passenger Class')
        st.plotly_chart(fig_pclass_survival)

    if st.sidebar.checkbox('Survival rate by passenger class'):
        fig_age_survival = px.histogram(data, x='Age', color='Survived', nbins=50, title='Age Distribution by Survival Status')
        st.plotly_chart(fig_age_survival)
    
    if st.sidebar.checkbox('Age distribution of passengers'):
        fig_age_survival = px.histogram(data, x='Age', color='Pclass', nbins=50, title='Age Distribution by Survival Status')
        return st.plotly_chart(fig_age_survival)

Visualize_data()

