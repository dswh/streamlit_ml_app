import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle


df_orig = pd.read_csv("cars24-car-price.csv")


encode_values={
  "fuel_type":  {"Diesel":1,"Petrol":2,"CNG":3,"LPG":4,"Electric":5  },
  "seller_type": {"Dealer":1,"Individual":2,"Trustmark Dealer":3     },
  "transmission_type": {"Manual":1,"Automatic":2  }
}


def model_pred(fuel_type, transmission_type,engine, seats):

    with open('car_pred', 'rb') as file:
        reg_model = pickle.load(file)

    new_X=[[2018.0, 1,  40000,   fuel_type, transmission_type, 19.70,  engine, 86.30,  seats]]
    return(reg_model.predict(new_X))


########   section 1 - input parameters   ########
st.set_page_config(layout="wide")

st.title("Car selling price prediction")


col1, col2 = st.columns(2)

fuel_type = col1.selectbox(" Select fuel type: ",
                     ['Diesel','Petrol','CNG','LPG','Electric'])

engine = col1.slider('Set the engine power', 500, 5000, 100)

transmission_type = col2.selectbox(" Select trainsmittion type: ",
                     ['Manual','Automatic'])
seats=col2.selectbox('No of seats', [4,5,6])

if(st.button("Predict Price")):
    fuel_type=encode_values["fuel_type"][fuel_type]
    transmission_type=encode_values["transmission_type"][transmission_type]

    price=model_pred(fuel_type, transmission_type,engine, seats)
    st.text("precited selling price in lakhs is: "+str(price))




########   section 2     ########

st.title("Understanding the data")

st.subheader("\n Here we will try to understand how the different features affect the selling price.\n ")
st.dataframe(df_orig.head(25))


########  section 3  ########

col1, col2 = st.columns(2)

########  column 1   ########

col1.subheader("Pairplot against selling price")
var1 = col1.selectbox(" Select Column for pairplot: ",
                     ['year','mileage','seller_type','km_driven','fuel_type','transmission_type','engine','max_power','seats'])
 
col1.text("selling price vs "+var1)

plot=sns.pairplot(y_vars=['selling_price'],x_vars=[var1], data=df_orig, height=8)
col1.pyplot(plot)


########  column 2   ########

col2.subheader("Histogram")
var2 = col2.selectbox(" Select Column for histogram: ",
                     ['mileage','year','seller_type','km_driven','fuel_type','transmission_type','engine','max_power','seats'])

bins=col2.slider('bins', 10, 100, 20)
col2.text("Histogram :"+var2)

fig = plt.figure()
sns.histplot(x = var2, data = df_orig, bins=bins)
col2.pyplot(fig)







