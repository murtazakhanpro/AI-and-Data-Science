import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config("std_form" ,layout="centered")

st.title("Student Form")
st.write("write your name and marks.")

with st.form("marks_form"):
    name = st.text_input("student name" , value="" )
    python = st.number_input("Enter Python marks(out of 100)" , min_value= 0 ,max_value= 100)
    c = st.number_input("Enter c marks(out of 100)", min_value=0 , max_value=100)
    r = st.number_input("Enter r marks(out of 100)" , min_value=0 , max_value=100)

    submit = st.form_submit_button("Submit")
    # marks = st.text_input("Marks")


def std_percentage(marks):
    return round((sum(marks) / 300)*100,2)
def std_grade(pct):
    # marks = 
    per = std_percentage(marks)
    if per >= 80:
        return "A"
    elif per >= 60:
        return "B"
    elif per >= 40:
        return "C"
    else :
        return "F"

if submit:
    marks = [python ,c,r]
    pct = std_percentage(marks)
    grade = std_grade(pct)

    st.subheader(f"Hello {name}")
    st.write(f" your percentage is {pct}")
    st.write(f"your grade is {grade}")