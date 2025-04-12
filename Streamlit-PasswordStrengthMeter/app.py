import streamlit as st
import re as r

# Set the title for the Streamlit app
st.title("Password Strength Checker")

# Input field for user's password.
user_input = st.text_input("Enter your password:", type="password")

def check_password(user_input: str):
    """
    Check the strength of the provided password according to several criteria.
    If the password fails a criteria, a warning is shown. The password is evaluated
    based on length, presence of both uppercase and lowercase letters, numbers, and special characters.
    
    If the password is a common (weak) password, an error is shown and further checks are skipped.
    
    Parameters:
        user_input (str): Password string provided by the user.
    """
    # Initialize the strength score
    score = 0

    # List of commonly used weak passwords.
    common_passwords = [
        "123456", "password", "123456789", "12345678", "12345",
        "1234567", "1234567890", "qwerty", "abc123", "password1",
        "111111", "123123", "admin", "letmein", "welcome",
        "monkey", "football", "iloveyou", "dragon", "sunshine",
        "princess", "qwerty123", "1q2w3e4r", "654321", "superman",
        "asdfgh", "trustno1", "hello", "whatever", "freedom",
        "passw0rd", "batman", "zaq12wsx", "master", "qazwsx",
        "login", "starwars", "michael", "shadow", "hannah",
        "jessica", "loveme", "password123", "1qaz2wsx", "charlie",
        "donald", "qwertyuiop", "maggie", "bismillah", "pokemon"
    ]
    
    # Check if the password is one of the common (weak) ones.
    if user_input.lower() in common_passwords:
        st.error("❌ Password is too common. Please choose a more secure password.")
        return  # Exit early if the password is common.
    
    # Check if the password length is at least 8 characters.
    if len(user_input) >= 8:
        score += 1
    else:
        st.warning("Password should be at least 8 characters long")
    
    # Check if the password contains both lowercase and uppercase letters.
    if r.search("[a-z]", user_input) and r.search("[A-Z]", user_input):
        score += 1
    else:
        st.warning("Password should contain both lowercase and uppercase letters")
    
    # Check if the password contains at least one digit.
    if r.search("[0-9]", user_input):
        score += 1
    else:
        st.warning("Password should contain at least one number")
    
    # Check if the password contains at least one special character.
    if r.search("[!@#$%^&*(),.?\":{}|<>]", user_input):
        score += 1
    else:
        st.warning("Password should contain at least one special character")
    
    # Provide feedback based on the strength score.
    if score == 4:
        st.success("✅ Password is strong!")
    elif score == 3:
        st.warning("⚠️ Password is medium strong. Try adding more variety (e.g., symbols or mixed case).")
    else:
        st.error("❌ Password is weak. Suggestions:")
        st.markdown("""
        - Use at least 8 characters  
        - Include **both uppercase and lowercase** letters  
        - Add at least **one number**  
        - Add at least **one special character** (like `@`, `#`, `!`, etc.)
        """)

# Only run the password check if user_input is not empty.
if user_input:
    check_password(user_input)

    



