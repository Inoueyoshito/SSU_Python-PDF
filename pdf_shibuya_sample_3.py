import os
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.lib.units import inch, mm, cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ファイルの指定
template_file = './resource/戸籍謄・抄本等請求書.pdf' # 既存のテンプレートPDF
output_file = './output/戸籍謄・抄本等請求書_result.pdf' # 完成したPDFの保存先
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
#〜 はじめにお読みください　〜
#本人及び本人の〜
cv.drawString(18*mm, h-36.5*mm, "1")
#宛先、宛先を記入した〜
cv.drawString(18*mm, h-41.5*mm, "1")
#手数料は、ゆうちょ銀行の〜
cv.drawString(18*mm, h-46.9*mm, "1")
#お急ぎの場合は〜
cv.drawString(18*mm, h-58*mm, "1")
#本籍
cv.drawString(92*mm, h-63.5*mm, "渋谷") #町
cv.drawString(92*mm, h-69.8*mm, "1") #丁目
cv.drawString(160*mm, h-63.5*mm, "渋谷") #番地
cv.drawString(160*mm, h-69.8*mm, "1") #番
#筆頭者
cv.drawString(50*mm, h-77.5*mm, "田中太郎")
#筆頭者フリガナ
cv.drawString(50*mm, h-84.3*mm, "タナカタロウ")
#どなたの戸籍が必要ですか
cv.drawString(50*mm, h-93.1*mm, "田中太郎")
#*1ヶ月以内に戸籍の届出をした方は記入してください
cv.drawString(110*mm, h-82.3*mm, "1") #月
cv.drawString(120.5*mm, h-82.3*mm, "1") #日
cv.drawString(134*mm, h-82.3*mm, "渋谷") #市・区・町
cv.drawString(167.5*mm, h-82.3*mm, "戸籍謄") #届出
#生年月日
cv.drawString(140*mm, h-89.5*mm, "2021") #年
cv.drawString(162.5*mm, h-89.5*mm, "1") #月
cv.drawString(176*mm, h-89.5*mm, "1") #日生
cv.drawString(147*mm, h-95.5*mm, "渋谷太郎") #旧姓
#戸籍
cv.drawString(81*mm, h-104.7*mm, "1") #全部事項(戸籍謄本)
cv.drawString(81*mm, h-112.2*mm, "1") #個人事項(戸籍抄本)
#改製原戸籍
cv.drawString(81*mm, h-119.8*mm, "1") #謄本
cv.drawString(81*mm, h-127*mm, "1") #抄本
#除籍
cv.drawString(81*mm, h-134.6*mm, "1") #謄本
cv.drawString(81*mm, h-141.8*mm, "1") #抄本
#附票
cv.drawString(81*mm, h-149.2*mm, "1") #全員
cv.drawString(81*mm, h-156.8*mm, "1") #個人
#注:徐附票の保存期限は5年です
cv.drawString(43*mm, h-169*mm, "東京都渋谷区渋谷1丁目1-1") #個人
#身分証明書
cv.drawString(151*mm, h-104.7*mm, "1")
#受理証明書
cv.drawString(136*mm, h-119.8*mm, "◯") #[届出の種類] 婚姻
cv.drawString(149.5*mm, h-119.8*mm, "◯") #[届出の種類] 離婚
cv.drawString(162.5*mm, h-119.8*mm, "◯") #[届出の種類] 出生
cv.drawString(176.5*mm, h-119.8*mm, "◯") #[届出の種類] 死亡
cv.drawString(163.5*mm, h-126.8*mm, "◯◯◯◯") #[届出の種類] その他
cv.drawString(157*mm, h-134.2*mm, "2021") #[届出日] 年
cv.drawString(172.5*mm, h-134.2*mm, "1") #[届出日] 月
cv.drawString(181*mm, h-134.2*mm, "1") #[届出日] 日
cv.drawString(157*mm, h-149.5*mm, "1") #[届出地]
#その他
cv.drawString(133*mm, h-157*mm, "◯◯◯◯◯◯◯◯◯◯") #一列目　欄
cv.drawString(179*mm, h-157*mm, "1") #一列目　通
cv.drawString(133*mm, h-164*mm, "◯◯◯◯◯◯◯◯◯◯") #二列目　欄
cv.drawString(179*mm, h-164*mm, "1") #二列目　通
#使い道
cv.drawString(41*mm, h-178.5*mm, "1") #パスポート
cv.drawString(74*mm, h-178.5*mm, "1") #戸籍の届出
cv.drawString(107*mm, h-178.5*mm, "1") #児童扶養手当
cv.drawString(145*mm, h-178.5*mm, "1") #公的年金申請
cv.drawString(41*mm, h-184*mm, "1") #名義変更など
cv.drawString(76*mm, h-184*mm, "◯◯◯◯◯◯") # ( )と
cv.drawString(107*mm, h-184*mm, "◯◯◯◯◯◯") # ( )の関係の証明が必要
cv.drawString(41*mm, h-190.5*mm, "1") #相続
cv.drawString(68*mm, h-196.5*mm, "渋谷死亡太郎") #亡くなった方( )
cv.drawString(107*mm, h-190.3*mm, "1") #出生から死亡まで
cv.drawString(144*mm, h-190.3*mm, "1") #(  　通ずつ)必要
cv.drawString(107*mm, h-195.7*mm, "1") #婚姻から死亡まで
cv.drawString(144*mm, h-195.7*mm, "1") #(  　通ずつ)必要
cv.drawString(107*mm, h-201.7*mm, "1") #死亡記載飲み必要
cv.drawString(107*mm, h-207.7*mm, "1") #□
cv.drawString(114.5*mm, h-207.7*mm, "◯◯◯") #(   )と
cv.drawString(138.5*mm, h-207.7*mm, "◯◯◯") #(   )の関係の証明が必要
cv.drawString(41*mm, h-214.5*mm, "1") #その他
cv.drawString(60*mm, h-214.5*mm, "◯◯◯◯◯◯◯◯◯◯◯◯◯◯◯◯◯◯") #その他 詳細
#請求するあなたの
cv.drawString(60*mm, h-224.5*mm, "東京都渋谷区渋谷1丁目1-1") #住所
cv.drawString(68*mm, h-232*mm, "タナカタロウ") #氏名フリガナ
cv.drawString(68.5*mm, h-238.5*mm, "田中太郎") #氏名
cv.drawString(110.5*mm, h-236.5*mm, "◯") #連絡先 自宅
cv.drawString(110.5*mm, h-240.5*mm, "◯") #連絡先 会社
cv.drawString(135.5*mm, h-237.5*mm, "0120") #連絡先　番号
cv.drawString(154*mm, h-237.5*mm, "1111") #番号　(    )
cv.drawString(173.5*mm, h-237.5*mm, "1111") #番号
#必要な戸籍に記載されている人から見て
cv.drawString(48*mm, h-244.5*mm, "◯") #本人
cv.drawString(65*mm, h-244.5*mm, "◯") #配偶者
cv.drawString(79*mm, h-244.5*mm, "◯") #子
cv.drawString(92.5*mm, h-244.5*mm, "◯") #父 母
cv.drawString(109.5*mm, h-244.5*mm, "◯") #祖父母
cv.drawString(123.5*mm, h-244.5*mm, "◯") #孫
cv.drawString(138.5*mm, h-244.5*mm, "◯") #代理人
cv.drawString(60*mm, h-250.5*mm, "◯◯◯◯◯◯◯◯◯◯◯◯") #その他



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
