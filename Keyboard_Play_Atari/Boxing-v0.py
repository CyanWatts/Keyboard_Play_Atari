import gym
import keyboard
import numpy as np
import time
'''
拳击Boxing-v0
wasd qezc:移动
jkl uio m,.:移动拳击（k是不动）
0：什么都不干
'''
total_reward = 0
env = gym.make('Boxing-v0')
state = env.reset()

action = 0

# 实际按键中只检测0，1，2，3 游戏中需要的按键
# 我添加了一个按键4，用于暂停
def abc(x):
    global action
    if x.event_type == "down" and x.name == '0':
        action = 0
    elif x.event_type == "down" and x.name == 'k':
        action = 1
    elif x.event_type == "down" and x.name == 'w':#UP
        action = 2
    elif x.event_type == "down" and x.name == 'd':#right
        action = 3
    elif x.event_type == "down" and x.name == 'a':#left
        action = 4
    elif x.event_type == "down" and x.name == 's':#down
        action = 5
    elif x.event_type == "down" and x.name == 'i':
        action = 10
    elif x.event_type == "down" and x.name == 'l':
        action = 11
    elif x.event_type == "down" and x.name == 'j':
        action = 12
    elif x.event_type == "down" and x.name == ',':#down hit
        action = 13
    elif x.event_type == "down" and x.name == 'o':
        action = 14
    elif x.event_type == "down" and x.name == 'u':
        action = 15
    elif x.event_type == "down" and x.name == '.':
        action = 16
    elif x.event_type == "down" and x.name == 'm':
        action = 17

    elif x.event_type == "down" and x.name == 'e':
        action = 6
    elif x.event_type == "down" and x.name == 'q':
        action = 7
    elif x.event_type == "down" and x.name == 'c':
        action = 8
    elif x.event_type == "down" and x.name == 'z':
        action = 9




# 添加hook，以检测用户的按键
keyboard.hook(abc)
total_reward = 0
while True:
    env.render()
    #while action == 4:
    #    time.sleep(0.1)
    #if action == 4:
    #    action = 0
    next_state,reward,done,_ = env.step(action)
    total_reward += reward
    #(x2,y2,p2) = preprocess(next_state)
    #print(action,total_reward,done,x2,y2,p2)
    time.sleep(0.1)
    if done:
        break

print("total reward:",end = '')
print(total_reward)
keyboard.wait()
