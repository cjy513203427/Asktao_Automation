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


#刷道（队长模式）
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

mousemove_click(701,214)#移动到刷道按钮

mousemove_click(989,634)#点击前往

time.sleep(10)#从其他地图走到轩辕庙陆压真人处花费10s

mousemove_click(1339,716)#点击便捷组队

mousemove_click(885,786)#点击创建队伍

mousemove_click(1121,781)#点击开始匹配

for i in range(1,10,1):
    teamFileName = 'judgeTeamCount'
    time.sleep(3)
    screenshot(391, 156, 1582, 853,teamFileName)#截图

    judgeTeamStr = characterRecognition('E:\\python_project\\Asktao_Automation\\resource\\'+teamFileName+'.png')#文字识别
    #每个人守护顺序不一样，按需修改
    if '斗阙长老' not in judgeTeamStr and '白骨长老' not in judgeTeamStr: #这两个守护不在，说明队伍已有三人，开始刷道
        mousemove_click(1411,227) #点击关闭按钮
        mousemove_click(701, 214)  # 移动到刷道按钮
        mousemove_click(989, 634)  # 点击前往
        mousemove_click(1332, 649)#点击【伏魔】我这就去
        break

    time.sleep(600)#休息十分钟后再次查看是否组到人

#刷道十轮之后的操作
for j in range(1,10,1):
    time.sleep(780)#平民伏魔一般780s之内，土豪伏魔有300s的，按需修改
    taskFileName = 'judgeTaskAccomplish'
    time.sleep(3)
    screenshot(391, 156, 1582, 853,taskFileName)
    judgeTaskStr = characterRecognition('E:\\python_project\\Asktao_Automation\\resource\\'+taskFileName+'.png')

    if '【伏魔】我这就去' in judgeTaskStr:
        mousemove_click(1332, 649)  # 点击【伏魔】我这就去
    else:
        time.sleep(60) #防止780s内还没有完成伏魔操作，再等60s，以防万一
        mousemove_click(1332, 649)  # 点击【伏魔】我这就去