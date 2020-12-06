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
env = gym.make('PongDeterministic-v4')
state = env.reset()
print(env.action_space)
action = 0

def abc(x):
    global action
    if x.event_type == "down" and x.name == '0':
        action = 0
    elif x.event_type == "down" and x.name == '1':
        action = 1
    elif x.event_type == "down" and x.name == '2':
        action = 2
    elif x.event_type == "down" and x.name == '3':
        action = 3
    elif x.event_type == "down" and x.name == '4':
        action = 4
    elif x.event_type == "down" and x.name == '5':
        action = 5
    #elif x.event_type == "down" and (action == 6 or x.name == '6'):
    #   action = 6
    #elif action != 6:
    #    action = 0

# 添加hook，以检测用户的按键
keyboard.hook(abc)
total_reward = 0
#for j in range(1000):
while True:
    env.render()
    #while action == 6:
    #    time.sleep(0.1)
    #if action == 6:
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
