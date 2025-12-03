from fastapi import APIRouter, UploadFile, File
from san.app.services.salary_service import analyze_salary_by_district
from san.app.responses.excel_response import generate_excel_response

router = APIRouter()

@router.post("/analyze/salary_by_district")
async def salary_by_district(file: UploadFile = File(...)):
    salary_stats = await analyze_salary_by_district(file)
    return generate_excel_response(salary_stats)
