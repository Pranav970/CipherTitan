import uvicorn
from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from rag_pipeline import EnterpriseRAGSystem

app = FastAPI(
    title="Secure Enterprise RAG API Gateway",
    version="1.0.0",
    description="Enforced Pre-Retrieval RBAC Routing Pipeline for Heterogeneous Silos"
)

# Initialize the core pipeline engine
rag_system = EnterpriseRAGSystem()

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    status: str
    user: str
    role: str
    routed_silo: str
    response: str
    citations: list[str]
    confidence_score: float

class ErrorResponse(BaseModel):
    status: str
    error: str
    citations: list[str]
    confidence_score: float

def verify_token(x_user_id: str = Header(..., description="The unique identity token of the querying employee")):
    if not x_user_id:
        raise HTTPException(status_code=401, detail="Missing X-User-ID authorization identity header.")
    return x_user_id

# === ADDED FOR PORTFOLIO VISIBILITY ===
@app.get("/", response_class=HTMLResponse)
async def portfolio_landing_page():
    """Renders a beautiful live landing page for recruiters visiting your portfolio link."""
    return """
    <html>
        <head>
            <title>Enterprise RAG Pipeline Gateway</title>
            <style>
                body { font-family: sans-serif; background: #0f172a; color: #f8fafc; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
                .card { background: #1e293b; padding: 40px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.3); text-align: center; max-width: 500px; }
                h1 { color: #3b82f6; margin-bottom: 10px; }
                p { color: #94a3b8; line-height: 1.6; }
                .btn { display: inline-block; background: #10b981; color: white; padding: 12px 24px; text-decoration: none; font-weight: bold; border-radius: 6px; margin-top: 20px; transition: 0.2s; }
                .btn:hover { background: #059669; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Enterprise RAG Core API Live</h1>
                <p>Welcome to the production deployment of the Pre-Retrieval RBAC Routing Pipeline. This live server executes Python-native vector operations, identity verification, and cross-silo queries.</p>
                <a href="/docs" class="btn">Explore Interactive API Docs (Swagger)</a>
            </div>
        </body>
    </html>
    """

@app.post("/api/v1/query", response_model=QueryResponse, responses={403: {"model": ErrorResponse}, 500: {"model": ErrorResponse}})
async def process_secure_query(request: QueryRequest, user_id: str = Depends(verify_token)):
    result = rag_system.execute_pipeline(user_id, request.query)
    
    if result["status"] == "SECURITY_VIOLATION":
        raise HTTPException(status_code=403, detail=result)
    elif result["status"] in ["SYSTEM_FAULT", "NO_CONTEXT"]:
        raise HTTPException(status_code=500, detail=result)
        
    return result

if __name__ == "__main__":
    print("[*] Starting Secure Gateway API Workers on port 8000...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
