from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.lib.units import inch, mm, cm

# A4縦(210*297mm)のCanvasを準備 -- (*1)
cv = canvas.Canvas('test.pdf', pagesize=portrait(A4))

# 矩形描画 --- (*2)
# PDFの座標を左下が(0, 0)となる
cv.rect(10*mm,250*mm,30*mm,30*mm)

# 線を描画 --- (*3)
cv.line(10*mm,220*mm,200*mm, 220*mm)

# 表を描画 --- (*4)
xlist = (10*mm, 80*mm, 200*mm)
ylist = (200*mm, 170*mm, 140*mm)
cv.grid(xlist, ylist)

# ファイルに保存 --- (*5)
cv.showPage()
cv.save()