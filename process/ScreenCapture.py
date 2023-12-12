# -*- coding: utf-8 -*-
import time

import win32gui, win32con
from PIL import ImageGrab
from PIL import ImageChops

class ScreenCapture:
    def __init__(self):
        self.hwnd = win32gui.FindWindow(0, "微信读书")
        if self.hwnd == 0:
            raise Exception("没有找到'微信读书'小程序")
        self.bound = win32gui.GetWindowRect(self.hwnd)
        self.rpx = self._rpx2px(self.bound[2] - self.bound[0])

    # rpx转px
    def _rpx2px(self, base):
        ratio = base / 750
        def _rpx(rpx):
            return rpx * ratio
        return _rpx

    # 截图
    def _getCapture(self):
        img = ImageGrab.grab(self.bound)
        return img
    
    # 切割
    def _splitCapture(self, img):
        quesImg = img.crop((self.rpx(85), self.rpx(460), self.rpx(670), self.rpx(590)))
        ansImg = img.crop((self.rpx(85), self.rpx(590), self.rpx(670), self.rpx(1055)))
        return quesImg, ansImg
    
    
    def run(self):
        img = self._getCapture()
        # img.show("test")
        return self._splitCapture(img)


def isSame(imgA, imgB):
    if imgA is None or imgB is None:
        return False
    diff = ImageChops.difference(imgA, imgB)
    if diff.getbbox():
        return False
    return True


if __name__ == "__main__":
    print("hello")
    sc = ScreenCapture()
    rate = 1.25
    sc.bound = [num * rate for num in sc.bound]
    print(sc.bound)
    tmpImg = None
    for i in range(0,200):
        img = sc._getCapture()
        if not isSame(tmpImg, img):
            img_name = f'../weread_pic/{i}.jpg'
            img.save(img_name)
            tmpImg = img
            print(img_name)
        time.sleep(1)
    # img.show()
    # quesImg = img.crop((0, 460, 517, 660))
    # quesImg.show()
    # print(sc.bound, rate)
    # qry, anw = sc.run()
    # qry.show()
