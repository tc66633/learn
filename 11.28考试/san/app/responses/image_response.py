import matplotlib.pyplot as plt
from fastapi.responses import FileResponse
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def generate_image_response(company_count):
    plt.figure(figsize=(10, 6))
    company_count.plot(kind='bar', color='skyblue')
    plt.title('按地区统计公司数量')
    plt.xlabel('地区')
    plt.ylabel('公司数量')
    plt.xticks(rotation=45)

    chart_path = "company_count_chart.png"
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    return FileResponse(chart_path, media_type='image/png', filename="company_count_chart.png")
