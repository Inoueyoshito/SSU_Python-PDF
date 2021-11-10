from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# フォントのパスを指定する --- (*1)
ttf_file = './ipaexm.ttf'
# フォントを登録する --- (*2)
pdfmetrics.registerFont(TTFont('IPAexGothic', ttf_file))

# A4縦のCanvasを作成 -- (*3)
w, h = portrait(A4)
cv = canvas.Canvas('pdf_sample_text.pdf', pagesize=(w, h))

# 描画フォントを指定 --- (*4)
font_size = 40
cv.setFont('IPAexGothic', font_size)

# 文字列を描画する --- (*5)
cv.drawString(20, h-100,  "こんにちは！")
cv.drawString(20, h-160, "日本語をPDFに描画するには")
cv.drawString(20, h-220, "フォントの登録が必要")

# ファイルに保存 --- (*6)
cv.showPage()
cv.save()
