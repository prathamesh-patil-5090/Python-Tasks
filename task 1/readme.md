
# Generating Report Cards from Excel (PDF form)

## Brief Explanation
1. We use pandas to read and preprocess the Excel file.  
2. We group by Student ID to calculate total and average scores.  
3. We use ReportLab to generate PDF files with a simple layout.  
4. Each report card displays the student’s name, total, average, and a table of subject scores.

## Python Scripts

### create_test_excel.py
```python
import pandas as pd

def create_test_excel():
    data = {
        'Student ID': [101, 101, 102, 102, 103, 103],
        'Name': ['Alice', 'Alice', 'Bob', 'Bob', 'Charlie', 'Charlie'],
        'Subject': ['Math', 'English', 'Math', 'English', 'Math', 'English'],
        'Subject Score': [85, 88, 90, 93, 78, 82]
    }
    df = pd.DataFrame(data)
    df.to_excel("student_scores.xlsx", index=False)

if __name__ == "__main__":
    create_test_excel()
```

### generate_report_cards.py
```python
import pandas as pd
import numpy as np
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

def generate_report_cards(excel_path):
    try:
        df = pd.read_excel(excel_path)
        df.dropna(subset=['Student ID', 'Name', 'Subject Score'], inplace=True)
    except Exception as e:
        print("Error reading Excel file:", e)
        return

    grouped = df.groupby('Student ID')
    for student_id, group_data in grouped:
        name = group_data['Name'].iloc[0]
        total_score = group_data['Subject Score'].sum()
        average_score = group_data['Subject Score'].mean()

        c = canvas.Canvas(f"report_card_{student_id}.pdf", pagesize=letter)
        c.drawString(50, 750, f"Report Card for {name}")
        c.drawString(50, 730, f"Total Score: {total_score}")
        c.drawString(50, 710, f"Average Score: {average_score:.2f}")

        table_data = [["Subject", "Score"]]
        for idx, row in group_data.iterrows():
            table_data.append([row['Subject'], row['Subject Score']])

        table = Table(table_data, colWidths=[200, 100])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        table.wrapOn(c, 50, 600)
        table.drawOn(c, 50, 600)
        c.save()

if __name__ == "__main__":
    generate_report_cards("student_scores.xlsx")
```