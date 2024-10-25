import streamlit as st
import pandas as pd

# Initialize cycle data storage
if "cycle_data" not in st.session_state:
    st.session_state["cycle_data"] = []

# Form for adding cycle data
st.title("Menstrual Cycle Tracker")

with st.form("cycle_form"):
    date = st.text_input("Date (DD-MM-YYYY)")
    day_of_cycle = st.number_input("Day of Cycle", min_value=1, step=1)
    note = st.text_input("Note")
    sex = st.text_input("Sex")
    bleeding = st.slider("Bleeding (0-4)", 0, 4, 0)
    fluid = st.text_input("Fluid Type")
    cramps = st.slider("Cramps (0-3)", 0, 3, 0)
    mood = st.text_input("Mood")

    submitted = st.form_submit_button("Add Entry")

    if submitted:
        if not date or not day_of_cycle or not note or not sex or not fluid or not mood:
            st.error("Please fill out all fields!")
        else:
            # Append new data to session state
            new_data = {
                "Date": date,
                "Day of Cycle": day_of_cycle,
                "Note": note,
                "Sex": sex,
                "Bleeding": bleeding,
                "Fluid": fluid,
                "Cramps": cramps,
                "Mood": mood,
            }
            st.session_state["cycle_data"].append(new_data)
            st.success("Data added successfully!")

# Display cycle data
st.subheader("Cycle Data")
if st.session_state["cycle_data"]:
    df = pd.DataFrame(st.session_state["cycle_data"])
    st.dataframe(df)
else:
    st.write("No data available.")
