import pdfplumber
import re

# 打开PDF文件
pdf_path = 'dzfp_24422000000180309825_中南大学湘雅三医院_20241207164501.pdf'
pdf = pdfplumber.open(pdf_path)

for page in pdf.pages:
    texts = page.extract_text()
    tables = page.extract_tables()
    print(texts)
    print(tables)
    发票号码 = re.findall(r"发票号码\s?{0,1}[:,：]\s?(.*?)\s", texts, re.I | re.S)[0]
    开票日期 = re.findall(r"开票日期\s?{0,1}[:,：]\s?(.*?)\s", texts, re.I | re.S)[0]
    名称 = re.findall(r"名称\s?{0,1}[:,：]\s?(.*?)\s", texts, re.I | re.S)
    购买方名称 = 名称[0]
    销售方名称 = 名称[1]
    识别号 = re.findall(r"识别号\s?{0,1}[:,：]\s?(.*?)\s", texts, re.I | re.S)
    购买方识别号 = 识别号[0]
    销售方识别号 = 识别号[1]
    items = re.findall(r"名称\s?[:,：]\s?(.*?)\s", texts, re.I | re.S)
    print(发票号码, 开票日期, 购买方名称, 销售方名称, 购买方识别号, 销售方识别号)