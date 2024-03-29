import streamlit as st
import os
import pandas as pd
import joblib as jb

heading_style = '''
<div style="color:red;" align='center'>
<h1>Heart stroke prediction</h1>
</div>
'''
def return_df(
    gender,
    age,
    hypertension,
    heart_disease,
	ever_married,
	work_type,
	Residence_type,
    avg_glucose_level,
    bmi,
    smoking_status):
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
gender=st.selectbox('Select your gender',['Male','Female'])
age=st.number_input('Enter your age',min_value=0)
hypertension=st.slider('Select your hypertension grade',0,1,0)
heart_disease=st.slider('Do you have heart disease?',0,1,0)
ever_married=st.selectbox('Are you Married ?',['Yes','No'])
work_type=st.selectbox('what is your work type?',['Private','Self-employed','Govt_job','children','Never_worked'])
Residence_type=st.selectbox('Give your residency type',['Urban','Rural'])
avg_glucose_level=st.number_input('What is your glucose level',min_value=0)
bmi=st.number_input('What is your body mass index',min_value=0)
smoking_status=st.selectbox('So you smoke?',['formerly smoked', 'never smoked', 'smokes','unknown'])
df=return_df(
    gender,
    age,
    hypertension,
	heart_disease,
    ever_married,    
	work_type,
    Residence_type,
	avg_glucose_level,
    bmi,
    smoking_status)
if st.button('Submit'):
	model=base_model()
	preds=model.predict(df)
	predictions=preds[0]
	if predictions==1:
		st.write('stroke')
	elif predictions==0:
	       st.write('no stroke')
	st.balloons()
	
