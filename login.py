import streamlit as st

# Function for checking login credentials
def check_credentials(username, password):
    # Simple static check for credentials
    if username == "abhay" and password == "abhay":
        return True
    return False

# Function to display the login page
def login_page():
    st.sidebar.header("Login Page")
    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Check credentials when login button is pressed
    if st.button("Login"):
        if check_credentials(username, password):
            st.success("Login successful!")
            # Set the session state for login status
            st.session_state['logged_in'] = True
            # Redirect to an external link after successful login
            st.markdown('[Click here to go to the Home page](https://homepy-bx2rsnhevyrwh5wxkvynmy.streamlit.app/)', unsafe_allow_html=True)
            st.rerun()  # Rerun the app (optional, can be used to refresh or move to next step)
        else:
            st.error("Invalid username or password")

# Main app function
def main_app():
    # Show the login page if not logged in
    if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
        login_page()
    else:
        # After successful login, redirect the user to an external link
        st.write("You are now logged in!")
        # Add additional logic here if you want to show something more after successful login.
        st.rerun()

# Run the app
if __name__ == "__main__":
    main_app()
