from sentence_transformers import SentenceTransformer
import chromadb
import pandas as pd
import numpy as np

class RecommendationEngine:
    def __init__(self, assessments_df):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("shl_assessments")
        
        # Prepare data for ChromaDB
        descriptions = assessments_df['description'].fillna('').tolist()
        embeddings = self.model.encode(descriptions).tolist()
        metadatas = assessments_df.to_dict(orient='records')
        
        self.collection.add(
            embeddings=embeddings,
            documents=descriptions,
            metadatas=metadatas,
            ids=[str(i) for i in range(len(descriptions))]
        )
        
        self.assessments = assessments_df
        
    def recommend(self, query, k=10):
        query_embedding = self.model.encode(query).tolist()
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=min(k, len(self.assessments))
        )
        
        # Extract and format results
        recommended_indices = [int(id) for id in results['ids'][0]]
        recommended_assessments = self.assessments.iloc[recommended_indices]
        
        return recommended_assessments[[
            'name', 'url', 'remote_support', 
            'adaptive_support', 'duration', 'test_type'
        ]]
