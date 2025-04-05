import pytest
from app.backend.recommendation_engine import RecommendationEngine
import pandas as pd

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'name': ['Java Test', 'Personality Test'],
        'description': ['Java programming assessment', 'Personality traits evaluation']
    })

def test_recommendation(sample_data):
    engine = RecommendationEngine(sample_data)
    results = engine.recommend("Need Java developer", 1)
    assert len(results) == 1
    assert "Java" in results.iloc[0]['name']
