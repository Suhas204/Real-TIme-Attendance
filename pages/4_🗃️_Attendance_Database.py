import streamlit as st

import pandas as pd
from datetime import datetime
import time

st.set_page_config(
    page_title= "Computer-Vision Based Attendance",
    page_icon= "🎥",
)

st.title("Attendance Database")
ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H-%M-%S")






df = pd.read_csv("Attendance/Attendance_"+ date + ".csv")
edit = st.sidebar.header("Edit")
form =  st.sidebar.form("form")
name = form.text_input("Name")
time_ = form.text_input("Time")
submit = form.form_submit_button()
if submit:
    new_data = {"NAME": name, "TIME": time_}
    df = df.append(new_data, ignore_index = True)
    df.to_csv("Attendance/Attendance_"+ date + ".csv", index = False)

st.dataframe(df.style.highlight_max(axis = 0))

