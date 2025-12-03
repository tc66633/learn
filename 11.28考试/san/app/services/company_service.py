import pandas as pd
from io import BytesIO

async def analyze_company_count(file):
    contents = await file.read()
    df = pd.read_csv(BytesIO(contents))
    df.columns = [col.strip().lower() for col in df.columns]
    print(df.columns)
    print(df.head())

    company_count = df.groupby('district')['companyid'].nunique()
    return company_count
