# Enterprise Secure RAG Submission Workspace

This package contains the complete solution for the **Enterprise RAG Intelligence Challenge**.

## Contents
1. `generate_test_data.py`: Multi-silo synthetic data pipeline constructor.
2. `rbac_engine.py`: Pre-retrieval identity verification policy layer.
3. `router.py`: Dual-pathway syntax-aware intent classification router.
4. `data_ingestion.py`: Document extraction framework for heterogeneous environments.
5. `rag_pipeline.py`: Main execution kernel backed by an In-Memory vector similarity database layout.
6. `app.py`: FastAPI enterprise service interface.

## Getting Started
1. Install dependencies: `pip install -r requirements.txt`
2. Generate the testing workspace environment on disk: `python generate_test_data.py`
3. Run or test the pipeline locally: `python rag_pipeline.py`
4. Deploy the operational API gateway microservice: `python app.py`
