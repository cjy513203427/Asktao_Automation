#coding=utf-8
import autopy
import time
import win32api
import win32con
#师门任务
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

mousemove_click(771, 203)  # 活动的坐标
mousemove_click(1009,295) #师门任务“前往”的坐标

time.sleep(20)#从其他地图走到师门花费20s

mousemove_click(1338,650) #点击【师门】师门任务按钮

time.sleep(260) #师门任务自动跑八环大概花费260s

mousemove_click(1449,377) #点击任务栏里 师门-巡逻(8/10)
time.sleep(7) #巡逻时间大概5s

mousemove_click(1338,650) #点击“开起来不错，买了”按钮

#买假货的情况
mousemove_click(1338,650) #点击离开

mousemove_click(1338,650) #点击“买上一颗”按钮

mousemove_click(1418,725) #点击使用

#师门二
#买到了宝物，然后去段铁心那里回答问题
