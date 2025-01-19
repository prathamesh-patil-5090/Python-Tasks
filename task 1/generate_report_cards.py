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