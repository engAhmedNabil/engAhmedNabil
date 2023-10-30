import joblib as jb
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
Model= jb.load("Model_Final.pkl")
Inputs= jb.load("Inputs_Final.pkl")
def prediction(Gender, Age, Driving_License,Region_Code, Previously_Insured, Vehicle_Age,Vehicle_Damage,Annual_Premium,Policy_Sales_Channel,Vintage):
    test_df=pd.DataFrame(columns=Inputs)
    test_df.at[0,'Gender']=gender_map(Gender) 
    test_df.at[0,'Age']= Age
    test_df.at[0,'Driving_License']= Driving_License_map(Driving_License)
    test_df.at[0,'Region_Code']= Region_Code
    test_df.at[0,'Previously_Insured']= Previously_Insured_map(Previously_Insured)
    test_df.at[0,'Vehicle_Age']= Vehicle_Age_map(Vehicle_Age)
    test_df.at[0,'Vehicle_Damage']= Vehicle_Damage_map(Vehicle_Damage)
    test_df.at[0,'Annual_Premium']= Annual_Premium
    test_df.at[0,'Policy_Sales_Channel']= Policy_Sales_Channel
    test_df.at[0,'Vintage']= Vintage
    result= Model.predict(test_df)
    return result[0]
def gender_map(x):
    gender={'Male':1,'Female':0}
    return gender[x]
def Driving_License_map(y):
    Driving_License={'yes':1,'no':0}
    return Driving_License[y]
def Previously_Insured_map(z):
    Previously_Insured={'yes':1,'no':0}
    return Previously_Insured[z]
def Vehicle_Age_map(a):
    Vehicle_Age={'more than 2 Years':3.0,'1-2 Year':2.0,'less than 1 Year':1.0}
    return Vehicle_Age[a]
def Vehicle_Damage_map(s):
    Vehicle_Damage={'yes':1,'no':0}
    return Vehicle_Damage[s]
def main():
    ## Setting up the page title and icon
    st.set_page_config(page_icon = '🏠 🏥',page_title= 'Health Insurance Prediction')
     # Add a title in the middle of the page using Markdown and CSS
    st.markdown("<h1 style='text-align: center;text-decoration: underline;color:GoldenRod'>Vehicle_Insurance</h1>", unsafe_allow_html=True)
    Gender=st.radio('Select Gender',['Male', 'Female'])
    Age=st.slider('Age', min_value=20, max_value=85, value=25,step=1)
    Driving_License=st.radio('Driving_License', ['yes', 'no'])
    Region_Code= st.selectbox('Pick Your Region_Code ', (28.,  3., 11., 41., 33.,  6., 35., 50., 15., 45.,  8., 36., 30.,26., 16., 47., 48., 19., 39., 23., 37.,  5., 17.,  2.,  7., 29.,46., 27., 25., 13., 18., 20., 49., 22., 44.,  0.,  9., 31., 12.,34., 21., 10., 14., 38., 24., 40., 43., 32.,  4., 51., 42.,  1.,52.))
    Previously_Insured=st.radio('Previously_Insured', ['yes', 'no'])
    Vehicle_Age=st.selectbox('Previously_Insured', ['more than 2 Years', '1-2 Year','less than 1 Year'])
    Vehicle_Damage=st.radio('Vehicle_Damage', ['yes', 'no'])
    Annual_Premium=st.number_input('Annual_Premium', min_value=2630, max_value=303339, value=31661,step=1)
    Policy_Sales_Channel= st.selectbox('Pick Your Policy_Sales_Channel', (26., 152., 160., 124.,  14.,  13.,  30., 156., 163., 157., 122.,19.,  22.,  15., 154.,  16.,  52., 155.,  11., 151., 125.,  25.,61., 1.,  86.,  31., 150.,  23.,  60.,  21., 121.,   3., 139.,12.,  29.,  55.,   7.,  47., 127., 153.,  78., 158.,  89.,  32., 8.,  10., 120.,  65.,   4.,  42.,  83., 136.,  24.,  18.,  56.,48., 106.,  54.,  93., 116.,  91.,  45.,   9., 145., 147.,  44.,109.,  37., 140., 107., 128., 131., 114., 118., 159., 119., 105.,135.,  62., 138., 129.,  88.,  92., 111., 113.,  73.,  36.,  28.,35.,  59.,  53., 148., 133., 108.,  64.,  39.,  94., 132.,  46.,81., 103.,  90.,  51.,  27., 146.,  63.,  96.,  40.,  66., 100.,95., 123.,  98.,  75.,  69., 130., 134.,  49.,  97.,  38.,  17.,110.,  80.,  71., 117.,  58.,  20.,  76., 104.,  87.,  84., 137.,126.,  68.,  67., 101., 115.,  57.,  82.,  79., 112.,  99.,  70.,2.,  34.,  33.,  74., 102., 149.,  43.,   6.,  50., 144., 143.,41., 141., 142.))
    Vintage=st.slider('Number of Days that associat with the company ', min_value=10, max_value=299, value=50,step=1)
    if st.button('predict'):
        results= prediction(Gender, Age, Driving_License,Region_Code, Previously_Insured, Vehicle_Age,Vehicle_Damage,Annual_Premium,Policy_Sales_Channel,Vintage)
        st.text(f"Is you interest Vehicle_Insurance : {int(results)}")   
if __name__ == '__main__':
    main()
