import paddleocr

# 初始化OCR模型
engine = paddleocr.PaddleOCR(use_gpu=True)
# 读取图像
img_path = 'D:\\code\\py\\ML\\OCR\\ti3.jpg'
img_path = 'D:\\code\\py\\ML\\OCR\\ti2.png'

# 进行OCR识别
result = engine.ocr(img_path)

# 打印识别结果
for line in result:
    for word_info in line :
        if len(word_info) == 2 and len(word_info[1]) == 2:
            print(word_info[1][0])