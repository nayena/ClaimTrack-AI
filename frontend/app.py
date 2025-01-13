# frontend\app.py
import streamlit as st

st.title("AI Advisor")
c1, c2, c3 = st.columns(3)
with c1:
    st.image("img/peep-21.png", width=325)

with c2:
    c4 = st.container()
    with c4:
        c4.page_link("pages/federal_aid.py", label="Federal Student Aid", icon="🤝")
        c4.page_link("pages/credit.py", label="Building Credit", icon="💳")
        c4.page_link("pages/retirement.py", label="Investing for Retirement", icon="💰")

with c3:
    st.image("img/peep-30.png", width=325) 
