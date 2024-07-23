import streamlit as st
import json, re
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

# NAIVE SEARCH
# filtered_df = df[df.location.str.contains(city_name)]

# FLEXIBLE SEARCH
def flexible_search(df, column, search_term):
    """
    Filter DataFrame based on a flexible search of a specified column.
    
    :param df: pandas DataFrame
    :param column: name of the column to search
    :param search_term: term to search for
    :return: filtered DataFrame
    """
    # Create a flexible pattern from the search term
    pattern = re.sub(r'\s+', '.*', re.escape(search_term.strip()))
    
    # Create a case-insensitive regular expression
    regex = re.compile(pattern, re.IGNORECASE)
    
    # Filter the DataFrame
    return df[df[column].str.contains(regex, na=False)]

filtered_df = flexible_search(df, 'location', city_name)

filtered_df.drop(columns=['page_number'], inplace=True)

st.title(f'Work in {city_name}')

st.dataframe(
    filtered_df,
    column_config={
        "url": st.column_config.LinkColumn()
    }    
)
# st.table(filtered_df)


