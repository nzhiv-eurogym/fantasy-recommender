import streamlit as st

st.title("Which Fantasy World is Right for You?")

st.write("Answer a few questions and get your fantasy book recommendation!")

# Questions
magic_world = st.selectbox("Do you like when magic is closely tied to the modern world?", ["Yes", "No"])
epic_scale = st.selectbox("Are you attracted to epic wars and the struggle between good and evil?", ["Yes", "No"])
politics = st.selectbox("Do you enjoy stories with intrigue, power struggles, and unexpected twists?", ["Yes", "No"])
monsters = st.selectbox("Are you interested in stories about monsters and monster hunters, like witchers?", ["Yes", "No"])
myths = st.selectbox("Are you interested in adventures where ancient myths come to life?", ["Yes", "No"])
portal_world = st.selectbox("Do you like stories where characters enter magical worlds through portals or wardrobes?", ["Yes", "No"])

# Recomendation
recommendation = ""

if magic_world == "Yes" and epic_scale == "No":
    recommendation = "Harry Potter (J.K. Rowling) – magic, wizarding school, modern world"
elif epic_scale == "Yes" and politics == "No" and portal_world == "No":
    recommendation = "The Lord of the Rings (J.R.R. Tolkien) – classic fantasy, epic battle between good and evil"
elif politics == "Yes":
    recommendation = "A Song of Ice and Fire / Game of Thrones (George R.R. Martin) – intrigues, dynasties, a harsh world"
elif monsters == "Yes":
    recommendation = "The Witcher (Andrzej Sapkowski) – monsters, monster hunters, Eastern European flavor"
elif myths == "Yes" and portal_world == "No":
    recommendation = "Percy Jackson (Rick Riordan) – teenage adventures, Greek mythology"
elif portal_world == "Yes":
    recommendation = "The Chronicles of Narnia (C.S. Lewis) – magical world, portals, allegories, fairytale adventures"
else:
    recommendation = "Try the classics — The Lord of the Rings (Tolkien) — or explore new fantasy worlds!"

if st.button("Get My Recommendation!"):
    st.markdown(f"### Your recommended fantasy world:\n**{recommendation}**")

