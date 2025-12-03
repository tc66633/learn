from fastapi.responses import StreamingResponse
import io
import pandas as pd

def generate_excel_response(salary_stats):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        salary_stats.to_excel(writer, index=False, sheet_name='Salary Stats')

    output.seek(0)
    return StreamingResponse(output, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', headers={"Content-Disposition": "attachment; filename=salary_by_district.xlsx"})
