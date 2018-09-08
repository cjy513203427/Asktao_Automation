#coding=utf-8
import autopy
import time
import win32api
import win32con
#竞技场
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

mousemove_click(771, 203)  # 活动的坐标

mousemove_click(1358,504)  # 竞技场"前往"的坐标

time.sleep(20)#从天墉城城中心/其他地图走到竞技使者花费20s

mousemove_click(1334, 650)  # 竞技使者对话框中的竞技场的坐标


#挑战完毕会出现对话窗口
for i in range(1,6,1):
    mousemove_click(664,706) #挑战试炼童子

    mousemove_click(1082,578) #确认

    mousemove_click(1528, 796)  # 战斗自动

    time.sleep(60)#挑战试炼童子预计60s




