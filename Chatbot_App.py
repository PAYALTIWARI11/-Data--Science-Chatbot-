import streamlit as st

# Title
st.title("🤖 Data Science Chatbot")

# Store past inputs and responses
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.chat_input("Ask me anything about data science!")

if user_input:
    # Append user input to session
    st.session_state.messages.append(("user", user_input))

    # Dummy chatbot response (replace this with your model or dataset logic)
    if "linear regression" in user_input.lower():
        response = "Linear regression is used to predict a continuous outcome based on input variables."
    elif "accuracy" in user_input.lower():
        response = "Accuracy is a metric used to evaluate classification models."
    else:
        response = "Sorry, I don’t understand that yet. Please ask something related to data science."

    st.session_state.messages.append(("bot", response))

# Display the conversation
for sender, msg in st.session_state.messages:
    if sender == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)
