import streamlit as st
import requests

st.title("EduAI Coach")
st.sidebar.header("User Registration")

# User registration form
name = st.sidebar.text_input("Name")
email = st.sidebar.text_input("Email")
subjects = st.sidebar.multiselect("Subjects", ["Math", "Science", "Language Arts"])

if st.sidebar.button("Register"):
    user_data = {"name": name, "email": email, "subjects": subjects}
    response = requests.post("http://127.0.0.1:5000/register", json=user_data)
    st.sidebar.success(response.json()["message"])

# Study plan
st.header("Your Personalized Study Plan")
user_id = st.number_input("Enter your user ID", min_value=0, step=1)
if st.button("Get Study Plan"):
    response = requests.get(f"http://127.0.0.1:5000/study-plan/{user_id}")
    plan = response.json().get("study_plan", [])
    for item in plan:
        st.write(f"Subject: {item['subject']}, Resource: [Link]({item['link']})")
