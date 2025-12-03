from fastapi import APIRouter, UploadFile, File
from san.app.services.company_service import analyze_company_count
from san.app.responses.image_response import generate_image_response

router = APIRouter()

@router.post("/analyze/company_count_chart")
async def company_count_chart(file: UploadFile = File(...)):
    company_count = await analyze_company_count(file)
    return generate_image_response(company_count)
