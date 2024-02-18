from fpdf import FPDF

title_1 = "Getting started"
title_2 = "improving..."

class PDF_reader(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        width = self.get_string_width(self.title)+6
        self.set_x((210-width)/2)
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        self.set_line_width(1)
        self.cell(width,9,title_1, new_x="LMARGIN",
                   new_y="NEXT", align="C", fill=True)
        self.ln(10)


    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 12)
        self.set_text_color(128)
        self.cell(0,10,f"Page {self.page_no()}", align="C")

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
pdf.set_title("Just a simple thing")
pdf.set_author("Rizzi")
pdf.print_chapter(1, title_1,"para.txt")
pdf.print_chapter(2, title_2,"para.txt")
pdf.output("sample_read.pdf")