from fastapi import FastAPI
from pydantic import BaseModel
from recommendation_engine import RecommendationEngine
import pandas as pd
import uvicorn

app = FastAPI()

# Load data and initialize engine
df = pd.read_csv("app/data/assessments.csv")
engine = RecommendationEngine(df)

class QueryRequest(BaseModel):
    text: str
    max_results: int = 10

@app.post("/recommend")
async def recommend_assessments(request: QueryRequest):
    try:
        results = engine.recommend(request.text, request.max_results)
        return results.to_dict(orient='records')
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
