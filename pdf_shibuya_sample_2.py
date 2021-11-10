import os
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.lib.units import inch, mm, cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ファイルの指定
template_file = './resource/転居届.pdf' # 既存のテンプレートPDF
output_file = './output/転居届_result.pdf' # 完成したPDFの保存先
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
cv.drawString(105*mm, h-47*mm, "2021")
cv.drawString(140*mm, h-47*mm, "12")
cv.drawString(175*mm, h-47*mm, "23")
cv.drawString(100*mm, h-59*mm, "恵比寿1丁目1-1")
cv.drawString(100*mm, h-71*mm, "本人")
cv.drawString(100*mm, h-83*mm, "渋谷1丁目1-1")
cv.drawString(100*mm, h-95*mm, "本人")
cv.drawString(100*mm, h-107*mm, "東京都")
cv.drawString(100*mm, h-119*mm, "渋谷太郎")
#転出者氏名(1~5)
cv.drawString(40*mm, h-159*mm, "渋谷父郎") #1
cv.drawString(40*mm, h-179*mm, "渋谷母郎") #2
cv.drawString(40*mm, h-198.5*mm, "渋谷一郎") #3
cv.drawString(40*mm, h-218*mm, "渋谷二郎") #4 
cv.drawString(40*mm, h-238*mm, "渋谷三郎") #5
#転出者氏名フリガナ (1~5)
cv.drawString(38*mm, h-149.5*mm, "シブヤチチロウ") #1
cv.drawString(38*mm, h-169*mm, "シブヤハハロウ") #2
cv.drawString(38*mm, h-188.5*mm, "シブヤイチロウ") #3
cv.drawString(38*mm, h-208*mm, "シブヤニロウ") #4
cv.drawString(38*mm, h-228*mm, "シブヤサンロウ") #5
#生年月日 明・大・昭・平・令 (1~5)
cv.drawString(74.5*mm, h-149.5*mm, "◯") #1 明
cv.drawString(81.5*mm, h-149.5*mm, "◯") #1 大
cv.drawString(88.5*mm, h-149.5*mm, "◯") #1 昭
cv.drawString(95.5*mm, h-149.5*mm, "◯") #1 平
cv.drawString(101.5*mm, h-149.5*mm, "◯") #1 令
#2
cv.drawString(74.5*mm, h-169*mm, "◯") #2 明
cv.drawString(81.5*mm, h-169*mm, "◯") #2 大
cv.drawString(88.5*mm, h-169*mm, "◯") #2 昭
cv.drawString(95.5*mm, h-169*mm, "◯") #2 平
cv.drawString(101.5*mm, h-169*mm, "◯") #2 令
#3
cv.drawString(74.5*mm, h-188.5*mm, "◯") #3 明
cv.drawString(81.5*mm, h-188.5*mm, "◯") #3 大
cv.drawString(88.5*mm, h-188.5*mm, "◯") #3 昭
cv.drawString(95.5*mm, h-188.5*mm, "◯") #3 平
cv.drawString(101.5*mm, h-188.5*mm, "◯") #3 令
#4
cv.drawString(74.5*mm, h-208*mm, "◯") #4 明
cv.drawString(81.5*mm, h-208*mm, "◯") #4 大
cv.drawString(88.5*mm, h-208*mm, "◯") #4 昭
cv.drawString(95.5*mm, h-208*mm, "◯") #4 平
cv.drawString(101.5*mm, h-208*mm, "◯") #4 令
#5
cv.drawString(74.5*mm, h-228*mm, "◯") #5明
cv.drawString(81.5*mm, h-228*mm, "◯") #5 大
cv.drawString(88.5*mm, h-228*mm, "◯") #5 昭
cv.drawString(95.5*mm, h-228*mm, "◯") #5 平
cv.drawString(101.5*mm, h-228*mm, "◯") #5 令
#生年月日 年 月 日 (1~5)
cv.drawString(76*mm, h-159*mm, "11") #1 年
cv.drawString(87.5*mm, h-159*mm, "11") #1 月
cv.drawString(98.5*mm, h-159*mm, "11") #1 年
#2
cv.drawString(76*mm, h-179*mm, "11") #1 年
cv.drawString(87.5*mm, h-179*mm, "11") #1 月
cv.drawString(98.5*mm, h-179*mm, "11") #1 日
#3
cv.drawString(76*mm, h-198.5*mm, "11") #1 年
cv.drawString(87.5*mm, h-198.5*mm, "11") #1 月
cv.drawString(98.5*mm, h-198.5*mm, "11") #1 日
#4
cv.drawString(76*mm, h-218*mm, "11") #4 年
cv.drawString(87.5*mm, h-218*mm, "11") #4　月
cv.drawString(98.5*mm, h-218*mm, "11") #4　日
#5
cv.drawString(76*mm, h-238*mm, "11") #5 年
cv.drawString(87.5*mm, h-238*mm, "11") #5 月
cv.drawString(98.5*mm, h-238*mm, "11") #5 日
#性別 男 女 (1~5)
cv.drawString(110*mm, h-149.5*mm, "◯") #1 男
cv.drawString(110*mm, h-162*mm, "◯") #1 女
#2
cv.drawString(110*mm, h-168.5*mm, "◯") #2 男
cv.drawString(110*mm, h-181.5*mm, "◯") #2 女
#3
cv.drawString(110*mm, h-188.5*mm, "◯") #3 男
cv.drawString(110*mm, h-201.5*mm, "◯") #3 女
#4
cv.drawString(110*mm, h-208*mm, "◯") #4 男
cv.drawString(110*mm, h-221*mm, "◯") #4 女
#5
cv.drawString(110*mm, h-228*mm, "◯") #5 男
cv.drawString(110*mm, h-240.5*mm, "◯") #5 女
#続柄 (1~5)
cv.drawString(120.5*mm, h-156*mm, "父") #1
cv.drawString(120.5*mm, h-175.5*mm, "母") #2
cv.drawString(120.5*mm, h-195*mm, "子") #3
cv.drawString(120.5*mm, h-214.5*mm, "子") #4
cv.drawString(120.5*mm, h-234*mm, "子") #5
#個人番号カード・住民基本台帳カード 有　無 (1~5)
cv.drawString(151.5*mm, h-150.5*mm, "◯") #1 有
cv.drawString(168.5*mm, h-150.5*mm, "◯") #1 無
#2
cv.drawString(151.5*mm, h-170*mm, "◯") #2 有
cv.drawString(168.5*mm, h-170*mm, "◯") #2 無
#3
cv.drawString(151.5*mm, h-189.5*mm, "◯") #3 有
cv.drawString(168.5*mm, h-189.5*mm, "◯") #3 無
#4
cv.drawString(151.5*mm, h-209.5*mm, "◯") #4 有
cv.drawString(168.5*mm, h-209.5*mm, "◯") #4 無
#5
cv.drawString(151.5*mm, h-228.5*mm, "◯") #5 有
cv.drawString(168.5*mm, h-228.5*mm, "◯") #5 無
#住民票コード (11マス) (1~5)
cv.drawString(129.5*mm, h-162*mm, "1") #1
cv.drawString(135.8*mm, h-162*mm, "1") #1
cv.drawString(142.1*mm, h-162*mm, "1") #1
cv.drawString(148.1*mm, h-162*mm, "1") #1
cv.drawString(154.2*mm, h-162*mm, "1") #1
cv.drawString(160.3*mm, h-162*mm, "1") #1
cv.drawString(166.6*mm, h-162*mm, "1") #1
cv.drawString(172.8*mm, h-162*mm, "1") #1
cv.drawString(178.9*mm, h-162*mm, "1") #1
cv.drawString(185.2*mm, h-162*mm, "1") #1
cv.drawString(191.3*mm, h-162*mm, "1") #1
#2
cv.drawString(129.5*mm, h-181.5*mm, "1") #2
cv.drawString(135.8*mm, h-181.5*mm, "1") #2
cv.drawString(142.1*mm, h-181.5*mm, "1") #2
cv.drawString(148.1*mm, h-181.5*mm, "1") #2
cv.drawString(154.2*mm, h-181.5*mm, "1") #2
cv.drawString(160.3*mm, h-181.5*mm, "1") #2
cv.drawString(166.6*mm, h-181.5*mm, "1") #2
cv.drawString(172.8*mm, h-181.5*mm, "1") #2
cv.drawString(178.9*mm, h-181.5*mm, "1") #2
cv.drawString(185.2*mm, h-181.5*mm, "1") #2
cv.drawString(191.3*mm, h-181.5*mm, "1") #2
#3
cv.drawString(129.5*mm, h-201.5*mm, "1") #3
cv.drawString(135.8*mm, h-201.5*mm, "1") #3
cv.drawString(142.1*mm, h-201.5*mm, "1") #3
cv.drawString(148.1*mm, h-201.5*mm, "1") #3
cv.drawString(154.2*mm, h-201.5*mm, "1") #3
cv.drawString(160.3*mm, h-201.5*mm, "1") #3
cv.drawString(166.6*mm, h-201.5*mm, "1") #3
cv.drawString(172.8*mm, h-201.5*mm, "1") #3
cv.drawString(178.9*mm, h-201.5*mm, "1") #3
cv.drawString(185.2*mm, h-201.5*mm, "1") #3
cv.drawString(191.3*mm, h-201.5*mm, "1") #3
#4
cv.drawString(129.5*mm, h-221*mm, "1") #4
cv.drawString(135.8*mm, h-221*mm, "1") #4
cv.drawString(142.1*mm, h-221*mm, "1") #4
cv.drawString(148.1*mm, h-221*mm, "1") #4
cv.drawString(154.2*mm, h-221*mm, "1") #4
cv.drawString(160.3*mm, h-221*mm, "1") #4
cv.drawString(166.6*mm, h-221*mm, "1") #4
cv.drawString(172.8*mm, h-221*mm, "1") #4
cv.drawString(178.9*mm, h-221*mm, "1") #4
cv.drawString(185.2*mm, h-221*mm, "1") #4
cv.drawString(191.3*mm, h-221*mm, "1") #4
#5
cv.drawString(129.5*mm, h-240.5*mm, "1") #5
cv.drawString(135.8*mm, h-240.5*mm, "1") #5
cv.drawString(142.1*mm, h-240.5*mm, "1") #5
cv.drawString(148.1*mm, h-240.5*mm, "1") #5
cv.drawString(154.2*mm, h-240.5*mm, "1") #5
cv.drawString(160.3*mm, h-240.5*mm, "1") #5
cv.drawString(166.6*mm, h-240.5*mm, "1") #5
cv.drawString(172.8*mm, h-240.5*mm, "1") #5
cv.drawString(178.9*mm, h-240.5*mm, "1") #5
cv.drawString(185.2*mm, h-240.5*mm, "1") #5
cv.drawString(191.3*mm, h-240.5*mm, "1") #5
#届出人 氏名
cv.drawString(98.5*mm, h-266.5*mm, "渋谷太郎")
#届出人 昼間の連絡先 (必ずご記入ください)
cv.drawString(98.5*mm, h-279*mm, "0120-1111-1111")

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
