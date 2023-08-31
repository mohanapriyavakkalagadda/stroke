import streamlit as st
import os
import pandas as pd
import joblib as jb
heading_style = '''
<div style="color:red;" align='center'>
<h1>Healthcare dataset stroke data</h1>
</div>
'''
def return_df(gender,age,hypertension,heart_disease,ever_married,work_type	,Residence_type,avg_glucose_level,bmi,smoking_status):
    kbn={
	'gender':[gender],
    'age':[age],
	'hypertension':[hypertension],
	'heart_disease':[heart_disease],
    'ever_married':[ever_married],
	'work_type':[work_type],
	'Residence_type':[Residence_type],
    'avg_glucose_level':[avg_glucose_level],
	'bmi':[bmi],
	'smoking_status':[smoking_status]
    }   
    final_df=pd.DataFrame(kbn)
    return final_df
def base_model():
    bmodel=jb.load(os.path.join('model.pkl'))
    return bmodel
st.markdown(heading_style, unsafe_allow_html=True)
gender=st.selectbox('This is gender', ['male','female'])
age=st.number_input('This is age',min_value=0)
hypertension=st.slider('This is hypertension', 0,1,0)
heart_disease=st.slider('This is heart_disease', 0,1,0)
ever_married=st.selectbox('This is ever_married',['yes','no'])
work_type=st.selectbox('This is work_type', ['Private','Self-employed','Govt_job'])
Residence_type=st.selectbox('This is Residence_type', ['Urban','Rural'])
avg_glucose_level=st.number_input('This is avg_glucose_level',min_value=0)
bmi=st.number_input('This is bmi', min_value=0)
smoking_status=st.selectbox('This is smoking_status', ['smokes','never smoked','formerly smoked','Unknown'])
df=return_df(gender,age,hypertension,heart_disease,ever_married,work_type	,Residence_type,avg_glucose_level,bmi,smoking_status)
if st.button('Submit'):
	model=base_model()
	preds=model.predict(df)
	predictions=preds[0]
	st.write(predictions)
	if predictions==1:
		st.write('detected')
	elif prediction==0:
		st.write('notdetected')