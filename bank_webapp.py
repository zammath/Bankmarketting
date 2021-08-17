import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from PIL import Image



lg_model=pickle.load(open('lg_model.pkl','rb'))
rf_model=pickle.load(open('rf_model.pkl','rb'))
sv_model=pickle.load(open('sv_model.pkl','rb'))
def classify(pred):
    if pred==0:
             return "you have deposit in bank"
    else:
             return "you dont have deposit in bank"




def main():
    img = Image.open('bank.png')
    img= img.resize((156,145))
    st.image(img,use_column_width=False)
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Deposit Prediction</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    activities=['RandomForest','Logistic Regression','Support vector machine']
    option=st.sidebar.selectbox('Which model would you like to use?',activities)
    st.subheader(option)
    age = st.number_input("your age",value=0)

    ## For gender
    job1 =('Choose...','management' ,'technician', 'entrepreneur' ,'blue-collar' ,'unknown',
                        'retired' ,'admin.' ,'services' ,'self-employed' ,'unemployed' ,'housemaid','student')
    job_options= list(range(len(job1)))
    job = st.selectbox("select job", job_options, format_func=lambda x: job1[x])

    ## For Marital Status
    mar_display = ('Choose...','No','Yes','divorced')
    mar_options = list(range(len(mar_display)))
    marital = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

    
    ## For edu
    edu_display = ('Choose...','tertiary' ,'secondary' ,'unknown', 'primary')
    edu_options = list(range(len(edu_display)))
    education = st.selectbox("Education",edu_options, format_func=lambda x: edu_display[x])
    
    
    balance = st.number_input("Enter your balance",value=0)

    ## For emp status
    housing_dis = ('Choose...','yes','no')
    house_options = list(range(len(housing_dis)))
    housing = st.selectbox("housing Status",house_options, format_func=lambda x: housing_dis[x])
    
    
    loan_disp = ('Choose...','yes','no')
    loan_options = list(range(len(loan_disp)))
    loan = st.selectbox("loan Status",loan_options, format_func=lambda x: loan_disp[x])

    contact_disp = ('Choose...','unknown' ,'cellular' ,'telephone')
    contact_options = list(range(len(contact_disp)))
    contact = st.selectbox("contact mode",contact_options, format_func=lambda x: contact_disp[x])

    ## Applicant Monthly Income
    day = st.number_input('Enter your date',value=0)

    month_disp = ('Choose...','may','jun','jul','aug','oct','nov','dec','jan','feb','mar','apr','sep')   
    month_options = list(range(len(month_disp)))
    month = st.selectbox("select month",month_options, format_func=lambda x: month_disp[x])

    duration = st.number_input('Enter your duration',value=0)
    campaign= st.number_input('campaign details',value=0) 
    previous= st.number_input('Enter your previous:',value=0)  
    
    poutcome_disp = ('Choose...','unknown','failure','other','success')
    pout_options = list(range(len(poutcome_disp)))
    poutcome= st.selectbox("select poutcome",pout_options, format_func=lambda x: poutcome_disp[x])
    result=""
    inputs=[[age,job,marital,education,balance,housing,loan,contact,day,month,duration,campaign,previous,poutcome]]
    if st.button('submit'):
        if option=='RandomForest':
            st.success(classify(rf_model.predict(inputs)))
        elif option=='Logistic Regression':
            st.success(classify(lg_model.predict(inputs)))
        else:
           st.success(classify(sv_model.predict(inputs)))

if __name__=='__main__':
    main()
