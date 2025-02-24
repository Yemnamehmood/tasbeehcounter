import streamlit as st

# Set page config for better appearance
st.set_page_config(page_title="Tasbeeh Counter", page_icon="📿", layout="centered")

# Custom CSS for a better UI
st.markdown("""
    <style>
    .main {
        background-color: #f4f4f4;
    }
    .counter-box {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        color: white;
        padding: 20px;
        border-radius: 10px;
        background-color: black;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        width: 200px;
        margin: 10px;
    }
    .tasbeeh-button {
        background-color: #4CAF50;
        color: white;
        font-size: 20px;
        padding: 15px 30px;
        border-radius: 50px;
        border: none;
        cursor: pointer;
        transition: 0.3s;
    }
    .tasbeeh-button:hover {
        background-color: #45a049;
    }
    .reset-button {
        background-color: #FF5733;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

# App Title
st.title("📿 Tasbeeh Counter")

# Session state to keep track of count
if 'count' not in st.session_state:
    st.session_state.count = 0

# Display the Counter
st.markdown('<div class="counter-box">{}</div>'.format(st.session_state.count), unsafe_allow_html=True)

# Increment Counter Function
def increment():
    st.session_state.count += 1

# Reset Counter Function
def reset():
    st.session_state.count = 0

# Buttons
col1, col2 = st.columns([1,1])
with col1:
    if st.button("📿 Click to Count", on_click=increment, key="tasbeeh", help="", use_container_width=True):
        pass
with col2:
    if st.button("🔄 Reset", on_click=reset, key="reset", help="Reset the counter", use_container_width=True):
        pass

# Footer
st.markdown("<br><hr><center>Made with ❤️ using Python & Streamlit</center>", unsafe_allow_html=True)
st.markdown("<br><hr><center> Made by Yemna Mehmood</center>",unsafe_allow_html=True)
