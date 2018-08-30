#coding=utf-8
import autopy
import time
import win32api
import win32con
from imageGrabUtil import screenshot
from baiduAipUtil import characterRecognition
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

#助人为乐
#time.sleep(5)
win32api.keybd_event(18,0,0,0)  #alt键位码是18
win32api.keybd_event(9,0,0,0)  #tab键位码是9
time.sleep(0.5)
win32api.keybd_event(13,0,0,0)  #enter键位码是13

win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
win32api.keybd_event(9,0,win32con.KEYEVENTF_KEYUP,0)
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
time.sleep(2)

def mousemove_click(x,y):
    autopy.mouse.smooth_move(x, y)
    autopy.mouse.click()


#帮助冯喜来
def fengXiLai(Y):
    mousemove_click(X1+200,Y+30) #鼠标移到按钮中央，点击冯喜来按钮
    for i in range(1,4,1):
        mousemove_click(1448,380)
        time.sleep(150) #打强盗、无名剑客平均时间150s
        mousemove_click(1515, 258)#跳过对话
        mousemove_click(1515, 258)
        time.sleep(15)
        mousemove_click(1448, 380)# 白邦芒处领赏

#帮助杨镖头
def yangBiaoTou(Y):
    mousemove_click(X1 + 200, Y + 30)
    for i in range(1,5,1):
        #和张老板对话,传递心意,找张老板,找玄武
        mousemove_click(1448, 380)#点任务栏 和张老板对话
        time.sleep(15)
        mousemove_click(1515, 258)  # 跳过对话

    mousemove_click(1448, 380)  # 点任务栏 寻找窃贼
    time.sleep(45)#和窃贼对战时间45s
    mousemove_click(1515, 258)  # 跳过对话

    for i in range(1,5,1):
        #向张老板复命,月老，莲花姑娘，张老板
        mousemove_click(1448, 380)  # 点任务栏 向张老板复命
        time.sleep(15)
        mousemove_click(1515, 258)  # 跳过对话

mousemove_click(771, 203)  # 活动的坐标

mousemove_click(1359,503) #前往的坐标

time.sleep(15)#从天墉城城中心/其他地图走到白帮忙花费15s

mousemove_click(1336,649) #领赏

#为了获取图片中指定文字的坐标，这里需要分开截图
helpedName1 = "helpedName1"
X1 = 1132
X2 = 1536
time.sleep(3)
screenshot(X1, 622, X2, 676,helpedName1)#截图

judgehelpedNameStr1 = characterRecognition('E:\\python_project\\Asktao_Automation\\resource\\'+helpedName1+'.png')#文字识别

helpedName2 = "helpedName2"

screenshot(X1, 690, X2, 741,helpedName2)#截图

judgehelpedNameStr2 = characterRecognition('E:\\python_project\\Asktao_Automation\\resource\\'+helpedName2+'.png')#文字识别
if '冯喜来' in judgehelpedNameStr1:
    fengXiLai(622)
elif '冯喜来' in judgehelpedNameStr2:
    fengXiLai(690)
elif '杨镖头' in judgehelpedNameStr1:
    yangBiaoTou(622)
elif '杨镖头' in judgehelpedNameStr2:
    yangBiaoTou(690)