var = 2
var = 3
print(var)


a = '1'
b = "1"
print(a + b)

a = 6
b = 3
a /= 2 * b
print(a)

x = 1
y = 2
z = x
x = y
y = z
print(x, y)

x = input(2)
y = input(4)
print(x + y)

x = int(input(2))
y = int(input(4))
x = x // y
y = y // x
print(y)


x = int(input(2))
y = int(input(4))

x = x / y
y = y / x

print(y)


x = int(input(11))
y = int(input(4))

x = x % y
x = x % y
y = y % x

print(y)

x = input(3)
y = int(input(6))

print(x * y)

z = y = x = 1
print(x, y, z, sep='*')




##genai old app.py

import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# load .env file
load_dotenv()

# connect Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# page setup
st.set_page_config(page_title="AI Study Notes Generator", page_icon="📚")

st.title("📚 AI Study Notes Generator")
st.write("Enter a topic and get AI-generated notes")

# user input
topic = st.text_input("Enter your topic")

# button
if st.button("Generate Notes"):
    if topic:

        prompt = f"""
        Explain {topic} in simple student-friendly language.
        Include:
        - Simple explanation
        - Key points
        - Short summary
        - 3 quiz questions
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        st.subheader("📘 Your Notes")
        st.write(response.text)

    else:
        st.warning("Please enter a topic")