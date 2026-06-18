import streamlit as st
import google.generativeai as genai
from datetime import datetime

today = datetime.today().strftime("%d %B %Y")
# Gemini API Key
# Gemini API Key
API_KEY = st.secrets["GEMINI_API_KEY"]
st.write("Secret Loaded:", "GEMINI_API_KEY" in st.secrets)
genai.configure(api_key=API_KEY)
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except:
    API_KEY = "AQ.Ab8RN6JDEg5xzqHpr3DxgFBkb6SeX62twCNiqqMrz_3rRcjEOw"
    

# Gemini Model
model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction="""
    You are an application writer.
    Never invent information.
    Use only user-provided details.
    Always follow the requested letter format.
    """
    )

# Website Title
st.title("🤖 AI Letter Generator")

st.write("Generate formal and informal letters using AI")

# User Inputs
name = st.text_input("Your Name")

address = st.text_area("Your Address")

receiver = st.text_input(
    "Receiver Name/Designation",
    placeholder="The Principal"
)

receiver_office = st.text_input(
    "Office/Institution",
    placeholder="MM Engineering College"
)

receiver_address = st.text_input(
    "Institution Address",
    placeholder="Mullana, Ambala"
)

subject = st.text_input("Subject")

purpose = st.text_area("Purpose of Letter")

letter_type = st.selectbox(
    "Letter Type",
    ["Formal", "Informal"]
)

length = st.selectbox(
    "Letter Length",
    ["Short", "Medium", "Long"]
)

# Generate Letter
if st.button("Generate Letter"):

    try:

        body_prompt = f"""
        Write a professional {letter_type} letter.

        Subject: {subject}

        Purpose:
        {purpose}

        Length: {length}

        Return ONLY the body paragraphs.
        Do not write address.
        Do not write date.
        Do not write receiver details.
        Do not write subject.
        Do not write closing.
        """

        response = model.generate_content(body_prompt)

        body = response.text.strip()

        letter = f"""
{address}

{today}

{receiver}
{receiver_office}
{receiver_address}

Dear Sir/Madam,

Subject: {subject}

{body}

Thank you for your time and consideration.

Sincerely,

{name}
"""

        st.subheader("Generated Letter")

        st.text_area(
            "Letter Output",
            value=letter,
            height=500
        )

    except Exception as e:
        st.exception(e)
