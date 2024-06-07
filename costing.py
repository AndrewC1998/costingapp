import streamlit as st
import math

# Function definition
def calculate_cost(n, g, p, s, h):
    return s * math.ceil(n / g) + p * (n - math.ceil(n / g)) * h

# Streamlit app
def main():
    st.title("Session Cost Calculator")

    st.write("""
    This app calculates the total cost of a session based on the number of people, group size, price per additional person, session cost for the instructor, and hours.
    """)
    
    with st.expander("Show formula"):
        st.markdown("""
        **Formula Used to Calculate the Cost:**

        \[
        \text{Total Cost} = s \cdot \lceil \frac{n}{g} \rceil + p \cdot (n - \lceil \frac{n}{g} \rceil) \cdot h
        \]

        where:
        - \( n \) is the number of people,
        - \( g \) is the number allowed in a group,
        - \( s \) is the session cost for the instructor,
        - \( p \) is the price per additional person,
        - \( h \) is the number of hours,
        - \( \lceil \cdot \rceil \) is the ceiling function.
        """)

    n = st.number_input("Number of people (n)", min_value=0, step=1, value=0)
    g = st.number_input("Number allowed in group (g)", min_value=1, step=1, value=8)
    s = st.number_input("Session cost for instructor (s)", min_value=0.0, step=0.01, value=48.0)
    p = st.number_input("Price per additional person (p)", min_value=0.0, step=0.01, value=10.0)
    h = st.number_input("Hours (h)", min_value=0.0, step=0.01, value=1.0)

    if st.button("Calculate Cost"):
        if n > 0:
            cost = calculate_cost(n, g, p, s, h)
            st.write(f"The total cost of the session is: £{cost:.2f}\n\nThe cost per person is: £{cost/n:.2f}")
        else:
            st.write("The number of people must be greater than 0 to calculate cost per person.")

if __name__ == "__main__":
    main()
