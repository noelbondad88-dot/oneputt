import streamlit as st

# BMI Calculator Function 

# input weight and height
weight = st.number_input("Enter your weight in kg:", min_value=0.0, format="%.2f")

# input height unit using radio button
height_unit = st.radio("Select your height unit:", options=["centimeters", "meters", "feet"])
height = st.number_input(f"Enter your height ({height_unit.lower()}):", min_value=0.0, format="%.2f")

# Calculate BMI when button is pressed
if st.button("Calculate BMI"):
    try:
        # Convert height to meters based on selected unit
        if height_unit == 'centimeters':
            height_m = height / 100
        elif height_unit == 'feet':
            height_m = height / 3.28
        else:
            height_m = height

        if height_m <= 0:
            st.error("Height must be greater than zero.") 
        else:
            bmi = weight / (height_m ** 2)
            st.success(f"Your BMI is {bmi:.2f}") 

            # Determine BMI category
        
            if bmi < 16:
                st.error("You are Extremely Underweight")
            elif 16 <= bmi < 18.5:
                st.warning("You are Underweight")
            elif 18.5 <= bmi < 25:
                st.success("You are Healthy")
            elif 25 <= bmi < 30:
                st.warning("You are Overweight")
            else:
                st.error("You are Extremely Overweight")
    except:
        st.error("Please enter valid numeric values.")

   
   

        

    