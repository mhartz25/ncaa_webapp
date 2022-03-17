import streamlit as st
import pandas as pd
import numpy as np
import os
import openpyxl



os.chdir('/Users/matthewhartz/python_practice/projects/ncaa_webapp/data')


#import data through pandas
data = pd.read_excel('mast.xlsx', sheet_name = 'Master Tab')
data = data.astype(str)


header = st.container()
BAN = st.container()
teams_chosen = st.container()

#set filepath through OS



with header:    
    st.title('2022 March Madness KO')

    st.write(data.dtypes)

#Status BAN
with BAN:
    st.header('% of People Left')
    st.write(data['Status'].value_counts())
    

with teams_chosen:
    st.header('Teams Chosen')
    st.text('Friday Team 1')
    st.write(data['Rd1Friday Team1']).value_counts()
    st.text('Friday Team 2')
    st.write(data['Rd1Friday Team2']).value_counts()