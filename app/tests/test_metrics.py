from app.backend.recommendation_engine import RecommendationEngine
import pandas as pd

def test_metrics():
    test_data = pd.DataFrame({
        'name': ['A', 'B', 'C'],
        'description': ['Java', 'Python', 'SQL']
    })
    
    engine = RecommendationEngine(test_data)
    results = engine.recommend("Java developer", 3)
    
    # Test recall
    relevant = ['A']
    recommended = results['name'].tolist()
    recall = len(set(recommended) & set(relevant)) / len(relevant)
    assert recall == 1.0
