import os
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.lib.units import inch, mm, cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ファイルの指定
template_file = './resource/住民票関係請求書.pdf' # 既存のテンプレートPDF
output_file = './output/住民票関係請求書_result.pdf' # 完成したPDFの保存先
tmp_file = './__tmp.pdf' # 一時ファイル

# A4縦のCanvasを作成 -- (*1)
w, h = portrait(A4)
cv = canvas.Canvas(tmp_file, pagesize=(w, h))

# フォントを登録しCanvasに設定 --- (*2)
font_size = 10
ttf_file = './ipaexm.ttf'
pdfmetrics.registerFont(TTFont('IPAexGothic', ttf_file))
cv.setFont('IPAexGothic', font_size)

# 文字列を描画する --- (*3)
cv.setFillColorRGB(0, 0, 0)
cv.drawString(55*mm, h-43*mm, "渋谷区　神宮前　１丁目１　１−１　１１１号室")
cv.drawString(40*mm, h-50*mm, "ツルタ ヒロム")
cv.drawString(40*mm, h-60*mm, "鶴田 啓")
cv.drawString(156*mm, h-53*mm, "1993")
cv.drawString(172*mm, h-53*mm, "7")
cv.drawString(182*mm, h-53*mm, "15")

# 一時ファイルに保存 --- (*4)
cv.showPage()
cv.save()

# テンプレートとなるPDFを読む --- (*5)
template_pdf = PdfFileReader(template_file)
template_page = template_pdf.getPage(0)

# 一時ファイルを読んで合成する --- (*6)
tmp_pdf = PdfFileReader(tmp_file)
template_page.mergePage(tmp_pdf.getPage(0))

# 書き込み先PDFを用意 --- (*7)
output = PdfFileWriter()
output.addPage(template_page)
with open(output_file, "wb") as fp:
  output.write(fp)

# 一時ファイル削除
os.remove(tmp_file)
