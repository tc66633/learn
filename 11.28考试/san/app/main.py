import uvicorn
from fastapi import FastAPI
from san.app.api.salary import router as salary_router
from san.app.api.company import router as company_router

app = FastAPI()

app.include_router(salary_router)
app.include_router(company_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000,reload=True)