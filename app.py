import numpy as np
import streamlit as st
import pickle

model = pickle.load(open('model.pickle','rb'))

st.set_page_config('Water Consumption App')

st.title('Predict Your Water Consumption')

apartment =  ['Studio','Cottage', '1BHK', '2BHK', '3BHK','Bungalow','Detached']
income = ['Low','Middle', 'Upper Middle', 'Rich']
facility = ['Swimming Pool','Garden', 'Fountain']

No_of_resident = st.number_input('Number of Resident',min_value=0,help='Number of people living in the apartment')
apartment      = st.selectbox('Apartment Type',apartment,help='Type of apartment')
Temperature    = st.number_input('Temperature',min_value=0)
Humidity       = st.number_input('Humidity',min_value=0)
Water_Price    = st.number_input('Water Price',min_value=0)
Per_Cons_Idx   = st.number_input('Period Consumption Index',help='how much water was used in a certain time compared to what is normal for that household.If a family normally uses 100 litres, but this time they used 150 litres, the index might be 1.5.')
Income         = st.selectbox('Income Level',income)
Guests         = st.number_input('Guests',min_value=0)
Amneties       = st.selectbox('Amenities',facility)
Appl_Usage     = st.number_input('Appliance_Usage',min_value=0)

dic_ap = {'1BHK': 0, '2BHK': 1, '3BHK': 2, 'Bungalow': 3, 'Cottage': 4, 'Detached': 5, 'Studio': 6}
dic_income = {'Low': 0, 'Middle': 1, 'Rich': 2, 'Upper Middle': 3}
dic_Amneties = {'Fountain': 0, 'Garden': 1, 'Jacuzzi': 2, 'None': 3, 'Swimming Pool': 4}

enc_apartment = dic_ap[apartment]
enc_income = dic_income[Income]
enc_Amneties = dic_Amneties[Amneties]

if st.button('Predict'):
           
        input_data = np.array([[
            No_of_resident,
            enc_apartment,
            Temperature,
            Humidity,
            Water_Price,
            Per_Cons_Idx,
            enc_income,
            Guests,
            enc_Amneties,
            Appl_Usage
        ]], dtype=float)

     
        pred = model.predict(input_data)

        st.success(f"Predicted Water Consumption: {float(pred[0]):.2f} litres")


