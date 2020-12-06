import gym
import keyboard
#import numpy as np
import time
'''
0、1停止
2、3轻上下移动
4、5重上下移动
'''
total_reward = 0
env = gym.make('LunarLander-v2')
state = env.reset()
print(env.action_space)
action = 0

def abc(x):
    global action
    if x.event_type == "down" and x.name == 'l':
        action = 0
    elif x.event_type == "down" and x.name == 'a':
        action = 1
    elif x.event_type == "down" and x.name == 'w':
        action = 2
    elif x.event_type == "down" and x.name == 'd':
        action = 3

    #elif x.event_type == "down" and (action == 6 or x.name == '6'):
    #   action = 6
    #elif action != 6:
    #    action = 0

# 添加hook，以检测用户的按键
keyboard.hook(abc)
total_reward = 0
#for j in range(1000):
i = 0
while True:

    env.render()
    if i==0:
        time.sleep(2)
    #while action == 6:
    #    time.sleep(0.1)
    #if action == 6:
    #    action = 0
    next_state,reward,done,_ = env.step(action)
    total_reward += reward
    #(x2,y2,p2) = preprocess(next_state)
    #print(action,total_reward,done,x2,y2,p2)
    time.sleep(0.05)
    i+=1
    if done:
        break
print("total reward:",end = '')
print(total_reward)
keyboard.wait()
