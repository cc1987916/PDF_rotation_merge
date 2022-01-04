from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def page_rotation(old_file, new_file):
    """
    PDF页面旋转
    :param old_file: 需要旋转的PDF文件
    :param new_file: 旋转后的PDF文件
    :return:
    """
    pdf = PdfFileReader(old_file)
    page_num = pdf.getNumPages()
    pdf_writer = PdfFileWriter()
    for i in range(page_num):
        # orientation = pdf.getPage(i).get('/Rotate')   # 获取页面的旋转角度
        size = pdf.getPage(i).mediaBox  # 获取页面大小值（长、宽）
        x, y = size.getUpperRight_x, size.getUpperRight_y
        if x > y:
            # 顺时针旋转90度  90的倍数
            page = pdf.getPage(i).rotateClockwise(90)
            # 逆时针旋转90度  90的倍数
            # page = pdf.getPage(i).rotateCounterClockwise(90)
            pdf_writer.addPage(page)
        else:
            # 不旋转
            page = pdf.getPage(i).rotateClockwise(0)
            pdf_writer.addPage(page)
    with open(new_file, 'wb') as f:
        pdf_writer.write(f)


ori_dir = r"C:\Users\GK\Desktop\test1"
#拿到文件夹内所有的pdf的绝对路径，存在列表中
pdf_path = [os.path.join(ori_dir, item) for item in os.listdir(ori_dir)]
print(pdf_path)
#创建pdfwriter
writer1 = PdfFileWriter()
#利用for循环，将pdf的每一页都添加到writer1中


for path in pdf_path:
    pdf = PdfFileReader(path)
    number = pdf.getNumPages()
    print(number)
    for i in range(number):
        size = pdf.getPage(i).mediaBox  # 获取页面大小值（长、宽）
        x, y = size.getUpperRight_x(), size.getUpperRight_y()
        if x > y:
            # 顺时针旋转90度  90的倍数
            page = pdf.getPage(i).rotateClockwise(90)
            # 逆时针旋转90度  90的倍数
            # page = pdf.getPage(i).rotateCounterClockwise(90)
            writer1.addPage(page)
        else:
            # 不旋转
            page = pdf.getPage(i).rotateClockwise(0)
            writer1.addPage(page)

with open(r"C:\Users\GK\Desktop\test2\new.pdf", "wb") as f:
    writer1.write(f)
