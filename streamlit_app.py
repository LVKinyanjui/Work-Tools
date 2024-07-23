import streamlit as st
import json
import pandas as pd


# Read data
with open('data/workwisse.jsonl', encoding='utf-8') as f:
    data = []
    for line in f:
        data.append(json.loads(line))

df = pd.DataFrame(data)

# if "city" not in st.session_state:
#     st.session_state.city = 'Nairobi'

st.text_input('Enter a city name', key='city')
city_name = st.session_state.city

filtered_df = df[df.location.str.contains(city_name)]
filtered_df.drop(columns=['page_number'], inplace=True)

st.title(f'Work in {city_name}')

st.dataframe(
    filtered_df,
    column_config={
        "url": st.column_config.LinkColumn()
    }    
)
# st.table(filtered_df)


