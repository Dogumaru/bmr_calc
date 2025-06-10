import streamlit as st

st.title("BMR and TDEE Calculator")

# Organize inputs in two columns
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Enter age in years:", min_value=0, max_value=120, step=1)
    weight = st.number_input("Enter weight in kilograms (kg):", min_value=0.1, format="%.2f")
    
with col2:
    height = st.number_input("Enter height in centimeters (cm):", min_value=0.1, format="%.2f")
    gender = st.selectbox("Gender:", ["male", "female"])

activity_level = st.selectbox("Activity level:", ["sedentary", "light", "moderate", "active"])
goal = st.selectbox("Goal:", ["maintain", "lose", "gain"])

if st.button("Calculate"):
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725
    }
    tdee = bmr * activity_multipliers[activity_level]

    if goal == 'lose':
        adjusted_tdee = tdee - 500
    elif goal == 'gain':
        adjusted_tdee = tdee + 500
    else:
        adjusted_tdee = tdee

    # Put results in a container for visual grouping
    with st.container():
        st.subheader("Results")
        st.write(f"**Estimated BMR:** {bmr:.2f} calories/day")
        st.write(f"**Estimated TDEE:** {tdee:.2f} calories/day")
        st.write(f"**Calorie goal to {goal} weight:** {adjusted_tdee:.2f} calories/day")
