import streamlit as st

# Initialize OpenAI API with your API key
import openai
openai.api_key = "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"

# Define a function to generate a response from GPT-3 y montar
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=1024, n=1,stop=None, temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return message

# Create a Streamlit app
st.title("Chat with GPT-3")

# Add a text input field for the user to enter their message
user_input = st.text_input("Enter your message here:")

# When the user submits their message, generate a response from GPT-3 and display it
if st.button("Send"):
    prompt = f"User: {user_input}\nBot:"
    bot_response = generate_response(prompt)
    st.text_area("Bot's response:", value=bot_response, height=200, max_chars=None, key=None)
