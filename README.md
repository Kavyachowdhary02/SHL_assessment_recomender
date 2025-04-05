# SHL Assessment Recommendation System

An intelligent system that recommends relevant SHL assessments based on job descriptions.

## Features
- Natural language processing of job descriptions
- Recommends up to 10 relevant assessments
- Includes key assessment attributes
- Web interface and API endpoints

## Setup
1. Clone this repository
2. Install requirements: `pip install -r requirements.txt`
3. Run backend: `uvicorn app.backend.main:app --reload`
4. Run frontend: `streamlit run app/frontend/streamlit_app.py`

## API Endpoints
- POST `/recommend` - Get assessment recommendations
