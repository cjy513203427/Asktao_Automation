#coding=utf-8

from PIL import ImageGrab
# 参数说明
# 第一个参数 开始截图的x坐标
# 第二个参数 开始截图的y坐标
# 第三个参数 结束截图的x坐标
# 第四个参数 结束截图的y坐标
def screenshot(x1,y1,x2,y2,filename):
    bbox = (x1, y1, x2, y2)
    im = ImageGrab.grab(bbox)

    # 参数 保存截图文件的路径
    im.save('E:\\python_project\\Asktao_Automation\\resource\\'+filename+'.png')