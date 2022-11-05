from fpdf import FPDF
from bill import Bill, Flatmate


class PDFreport:
    def __init__(self, filename):
        self.filename = filename

    def create_file(self, bill, *flatmates):
        if not isinstance(bill, Bill):
            raise TypeError("Bill must be an instance of Bill class")

        if any(not isinstance(flatmate, Flatmate) for flatmate in flatmates):
            raise TypeError("Flatmate must be an instance of Flatmate class")

        """
        orientation='P' - portrait, vertical file
        format A5
        unit='pt' - unit: points
        """

        pdf = FPDF(orientation='P', unit='pt', format='A5')
        pdf.add_page()
        pdf.set_font(family='times', size=24, style='B')

        pdf.cell(w=0, h=80, txt='', ln=1)

        pdf.cell(w=80, h=80, txt='')
        pdf.set_text_color(220, 50, 50)  # red
        pdf.cell(w=150, h=80, txt=f"Bill - {bill.period}", align='C', ln=1)

        pdf.set_text_color(0, 0, 0)
        pdf.set_font(family='times', size=16, style='B')
        pdf.cell(w=100, h=40, txt='')
        pdf.cell(w=60, h=40, txt='Period:')
        pdf.cell(w=60, h=40, txt=bill.period, ln=1)

        pdf.set_font(family='times', size=14, style='B')
        pdf.cell(w=100, h=25, txt='')
        pdf.cell(w=100, h=25, txt="Name")
        pdf.cell(w=100, h=25, txt="Amount", ln=1)
        pdf.set_font(family='times', size=14)
        for flatmate in flatmates:
            pdf.cell(w=100, h=25, txt='')
            pdf.cell(w=100, h=25, txt=flatmate.name)
            pdf.cell(w=100, h=25, txt=str(flatmate.how_many_pay(bill)), ln=1)

        pdf.set_font(family='times', size=14, style='BI')
        pdf.cell(w=100, h=25, txt='')
        pdf.cell(w=100, h=25, txt="Total amount", border=0)
        pdf.cell(w=60, h=25, txt=str(bill.amount), border=0, ln=1)

        pdf.output(self.filename)
