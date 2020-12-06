import gym
import keyboard
import numpy as np
import time
'''
a left
d right  
s stop(nop)
p pause
b begin
'''
total_reward = 0
env = gym.make('Breakout-v0')
state = env.reset()

action = 0
#PongDeterministic-v4
def preprocess(img):        ###针对Breakout-v0'游戏的一个预处理函数（用来辅助print）
    img_temp = img.mean(axis = 2)
    x = -1
    y = -1
    if len(np.where((img_temp[100:189,8:152])!= 0)[0]) != 0:
        x = np.where((img_temp[100:189,8:152])!= 0)[0][0]
        y = np.where((img_temp[100:189,8:152])!= 0)[1][0]
    if len(np.where((img_temp[193:,8:152])!= 0)[0]) != 0:
        x = -2
        y = -2
    p = int(np.where(img_temp[191:193,8:152])[1].mean() - 7.5)
    #return img_temp
    return (x,y,p)

# 实际按键中只检测0，1，2，3 游戏中需要的按键
# 我添加了一个按键4，用于暂停
def abc(x):                                         #x为hook传入的键盘事件keyboard.KeyboardEvent    #3个常用参数：event_type、scan_code(按键号)、name
    global action
    if x.event_type == "down" and x.name == 's':    #event_type == "down" down即按下的意思   x.name:按键名字
        action = 0
    elif x.event_type == "down" and x.name == 'b':
        action = 1
    elif x.event_type == "down" and x.name == 'd':
        action = 2
    elif x.event_type == "down" and x.name == 'a':
        action = 3
    elif x.event_type == "down" and (action == 4 or x.name == 'p'):
        action = 4
    elif action != 4:
        action = 0

# 添加hook，以检测用户的按键
keyboard.hook(abc)      # keyboard.hook(callback)按下任何按键时，都会调用callback，其中一定会传一个值，就是键盘事件，此处abc就是callback函数

total_reward = 0
for j in range(1000):
    env.render()
    while action == 4:
        time.sleep(0.1)
    if action == 4:
        action = 0
    next_state,reward,done,_ = env.step(action)
    total_reward += reward
    (x2,y2,p2) = preprocess(next_state)
    print(action,total_reward,done,x2,y2,p2)
    time.sleep(0.1)
    if done:
        break
keyboard.wait()
