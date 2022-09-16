import streamlit
streamlit.header("Anvi's Kitchen")
streamlit.title("My first streamlit app")
streamlit.title("Rich Chocolate coffee Cake")
streamlit.title("Pomogranade Juice")

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
