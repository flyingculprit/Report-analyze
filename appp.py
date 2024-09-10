import streamlit as st
from openai import OpenAI
from PyPDF2 import PdfReader

def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def analyze_text_with_openai(api_key, text):
    client = OpenAI(api_key=api_key)
    messages = [
        {"role": "system", "content": "You are a helpful assistant that analyzes medical reports."},
        {"role": "user", "content": f"Analyze the following medical report text and provide insights and potential diagnosis:\n\n{text}"}
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )
    report = response.choices[0].message.content.strip()
    return report

def extract_insights_from_report(report_text):
    insights = []

    # Example of extracting key metrics
    if "blood pressure" in report_text.lower():
        insights.append("Blood Pressure levels noted.")
    if "heart rate" in report_text.lower():
        insights.append("Heart Rate information extracted.")

    # Example of identifying potential concerns
    if "high" in report_text.lower() or "elevated" in report_text.lower():
        insights.append("Elevated values detected in the report.")
    if "low" in report_text.lower() or "decreased" in report_text.lower():
        insights.append("Low values detected in the report.")

    # Example of providing recommendations
    if "cholesterol" in report_text.lower():
        insights.append("Recommendation: Follow up with cholesterol-lowering measures if values are high.")
    
    # You can add more rules and checks based on common medical terms and conditions

    return insights

st.title('Medical Report Analyzer')

api_key_input = st.text_input("Enter your OpenAI API key", type="password")

if api_key_input:
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        
        text = extract_text_from_pdf(uploaded_file)

        
        st.write("Analyzing text with OpenAI...")
        report = analyze_text_with_openai(api_key_input, text)
        
        st.header("Analysis Report")
        st.write(report)
        
        st.header("Additional Insights")
        insights = extract_insights_from_report(report)
        for insight in insights:
            st.write("- " + insight)
else:
    st.warning("Please add your OpenAI API key. You can get it from [OpenAI website](https://beta.openai.com/signup/).")