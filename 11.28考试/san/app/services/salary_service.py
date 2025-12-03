import pandas as pd
from io import BytesIO

async def analyze_salary_by_district(file):
    contents = await file.read()
    df = pd.read_csv(BytesIO(contents))

    salary_stats = df.groupby('district')['salary'].agg(['mean', 'min', 'max']).reset_index()
    return salary_stats
