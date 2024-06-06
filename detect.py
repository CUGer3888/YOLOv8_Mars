from ultralytics import YOLO

import cv2
from PIL import Image
from ultralytics import YOLO
if __name__ == "__main__":
    # 加载YOLOv8模型
    model = YOLO("best.pt")
    im1 = Image.open("045.jpg")
    results = model.predict(source=im1, save=True)  # save plotted images
"""
pic_list = ["","",""] #如果得到的图片多，使用这个方法。加入图片的地址
model = YOLO("best.pt")
for i in pic_list:
    img = Image.open(i)
    results = model.predict(source=im1, save=True)
"""