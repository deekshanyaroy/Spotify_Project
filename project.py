# Here to start writing code'

# checking

import sqlite3
import pandas as pd
import streamlit as st

st.set_page_config(layout='wide')

#path to sql database
database_path = 'C:\Users\deeks\OneDrive\Desktop\WFU_MSBA\Data Management\Spotify_Project.songs.db'

#connec to sql db
connection = sqlite3.connect(database_path)

#create cursor object
cursor = connection.cursor()

#write sql query
