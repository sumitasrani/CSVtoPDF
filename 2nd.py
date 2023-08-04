from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

with open("topics.csv", 'r') as file:
    for i, row in enumerate(file):
        v = [file.readline()]
        v1 = v[0].split(',')
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=24)
        pdf.cell(w=0, h=12, txt=f"{v1[1]}", align='L', ln=1)
        pdf.line(10,21,200,21)
        x = int(v1[2])
        for j in range(x-1):
            pdf.add_page()

    pdf.output("out.pdf")






