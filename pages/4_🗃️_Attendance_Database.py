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

import streamlit as st
from streamlit_autorefresh import st_autorefresh

# Run the autorefresh about every 2000 milliseconds (2 seconds) and stop
# after it's been refreshed 100 times.
count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

# The function returns a counter for number of refreshes. This allows the
# ability to make special requests at different intervals based on the count
# if count == 0:
#     st.write("Count is zero")
# elif count % 3 == 0 and count % 5 == 0:
#     st.write("FizzBuzz")
# elif count % 3 == 0:
#     st.write("Fizz")
# elif count % 5 == 0:
#     st.write("Buzz")
# else:
#     st.write(f"Count: {count}")


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

