from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# PDFを日本語で使えるように登録
pdfmetrics.registerFont(UnicodeCIDFont("HeiseiMin-W3"))

packet = io.BytesIO()

# 書き込む準備
can = canvas.Canvas(packet, pagesize=letter)

# 書き込む内容を記載
# Hello worldと出力
can.drawString(100, 500, "Hello world")

# フォントの名前とサイズを指定してこんにちはと出力
can.setFont("HeiseiMin-W3", 30)
can.drawString(100, 400, "こんにちは")


can.save()

packet.seek(0)
new_pdf = PdfFileReader(packet)

# テンプレートのPDFを読み込む
existing_pdf = PdfFileReader(open("sample.pdf", "rb"))

output = PdfFileWriter()
page = existing_pdf.getPage(0)
page2 = new_pdf.getPage(0)
page.mergePage(page2)
output.addPage(page)
outputStream = open("output.pdf", "wb")
output.write(outputStream)
outputStream.close()
