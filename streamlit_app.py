import streamlit
streamlit.header("Anvi's Kitchen")
streamlit.title("My first streamlit app")
streamlit.title("Rich Chocolate coffee Cake")
streamlit.title("Pomogranade Juice")
streamlit.title("Chocolate Bownie")
streamlit.title("CheakPee Salad")


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

import requests

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())
# normalise the data
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display in the form of table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("Fruit load list contains:")
streamlit.dataframe(my_data_row)

add_fruit_choice = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('The user wants to add ', add_fruit_choice)

#insert row into table
my_cur.execute("insert into fruit_load_list values ('from_streamlit')")
