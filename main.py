# main.py
import streamlit as st

# --- Page Configuration (Optional but good practice) ---
st.set_page_config(
    page_title="My Simple Streamlit App",
    page_icon="🎈", # You can use an emoji or a URL to an icon
    layout="centered" # or "wide"
)

# --- App Title ---
st.title("🎈 My Simple Streamlit App")

# --- Introduction Text ---
st.write("Welcome to this basic Streamlit application!")
st.markdown("---") # Adds a horizontal rule

# --- Interactive Widget: Slider ---
st.subheader("Interactive Slider")
# Create a slider that goes from 0 to 100, with a default value of 25
# The key 'age_slider' is optional but can be useful for accessing the widget's state
age = st.slider("Select your age:", min_value=0, max_value=100, value=25, key="age_slider")

# --- Displaying Output ---
# Display the current value of the slider
st.write(f"You selected: **{age}** years old.")

st.markdown("---")

# --- Another Example: Text Input ---
st.subheader("Text Input Example")
user_name = st.text_input("What's your name?", placeholder="Enter your name here")

if user_name: # Only display if the user has entered something
    st.write(f"Hello, **{user_name}**! Nice to meet you.")

# --- Another Example: Button ---
st.subheader("Button Example")
if st.button("Click Me!"):
    st.balloons() # Fun little animation when button is clicked
    st.success("You clicked the button! 🎉")

# --- Displaying Data (Example with a simple dictionary) ---
st.markdown("---")
st.subheader("Displaying Data")
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 25, 35],
    "City": ["New York", "London", "Paris"]
}
st.write("Here's some sample data as a DataFrame:")
st.dataframe(data) # Displays the dictionary as a table (like pandas DataFrame)

st.caption("This is a simple Streamlit app. Enjoy exploring!")

# To run this app:
# 1. Save this code as main.py
# 2. Open your terminal or command prompt.
# 3. Navigate to the directory where you saved main.py.
# 4. Run the command: streamlit run main.py
