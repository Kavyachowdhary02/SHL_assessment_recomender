import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")

st.title("🎯 SHL Assessment Recommendation System")
st.markdown("Enter a job description to get relevant SHL assessments")

# Input section
col1, col2 = st.columns(2)
with col1:
    query = st.text_area("Job Description:", height=150)
with col2:
    time_limit = st.slider("Maximum Duration (minutes):", 10, 120, 60)
    max_results = st.slider("Number of Recommendations:", 1, 10, 5)

if st.button("Get Recommendations"):
    if query:
        with st.spinner("Finding best assessments..."):
            try:
                response = requests.post(
                    "http://localhost:8000/recommend",
                    json={
                        "text": f"{query} duration under {time_limit} minutes",
                        "max_results": max_results
                    }
                )
                
                if response.status_code == 200:
                    results = pd.DataFrame(response.json())
                    st.success(f"Found {len(results)} assessments")
                    
                    # Display results with formatting
                    results['url'] = results['url'].apply(
                        lambda x: f'<a href="{x}" target="_blank">View Assessment</a>'
                    )
                    st.write(results.to_html(escape=False), unsafe_allow_html=True)
                else:
                    st.error(f"API Error: {response.text}")
            except Exception as e:
                st.error(f"Connection failed: {str(e)}")
    else:
        st.warning("Please enter a job description")
