from fpdf import FPDF

title_1 = "Getting started"
title_2 = "improving..."

class PDF_reader(FPDF):
    def header(self):
        pass

    def footer(self):
        pass

    def chapter_title(self, num, label):
        self.set_font("helvetica", "", 12)
        self.set_fill_color(200,220,255)
        self.cell(0,6,f"Chapter {num} : {label}",
                   new_x="LMARGIN", new_y="NEXT", align="L", fill=True)
        

    def chapter_body(self, filepath):
        with open(filepath, "rb") as fp:
            txt = fp.read().decode('latin-1')
        self.set_font("Times", size=12)
        self.multi_cell(0,5, txt)
        self.ln()
        self.set_font(style="I")
        self.multi_cell(0,5, "(End of except)")
        

    def print_chapter(self,num, title, filepath):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(filepath)
        


pdf = PDF_reader()
pdf.print_chapter(1, title_1,"para.txt")
pdf.print_chapter(2, title_2,"para.txt")
pdf.output("sample_read.pdf")