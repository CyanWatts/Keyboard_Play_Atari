import gym
import keyboard
import numpy as np
import time
'''
！！！！！！！！！！！！！！Continuous！！！！！！！！！！！！！！！！
w   踩油门
s   松油门
a d 方向盘
j   踩刹车
k   松刹车
'''
EPSILON = 0.3
total_reward = 0
env = gym.make('CarRacing-v0')
state = env.reset()
print(env.action_space)
#action = 0

Steer = 0.
Throttle = 0.
Brake = 0.

def taction(joint, operation, name):
    if operation == "add":
        joint = min(joint + EPSILON, 1)
    elif name == "Steer":
        joint = max (joint - EPSILON, -1)
    else:
        joint = max (joint - EPSILON, 0)
    return joint


def abc(x):
    #print("abc")
    global Steer
    global Throttle
    global Brake

    if x.event_type == "down" and x.name == 'd':    #Steer add
        Steer = taction(Steer,"add","Steer")
    elif x.event_type == "down" and x.name == 'j':  #Brake add
        Brake = taction(Brake,"add","Brake")
    elif x.event_type == "down" and x.name == 'a':  #Steer sub
        Steer = taction(Steer,"sub","Steer")
    elif x.event_type == "down" and x.name == 'k':  #Brake sub
        Brake = taction(Brake,"sub","Brake")
    elif x.event_type == "down" and x.name == 'w':  #Throttle add
        Throttle = min(Throttle+0.2,1)
    elif x.event_type == "down" and x.name == 's':  #Throttle sub
        Throttle = taction(Throttle,"sub","Throttle")
    elif x.event_type == "down" and x.name == 'h':  #Steer zero
        Steer = 0


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
    action = np.array([Steer, Throttle, Brake])
    print(action)
    next_state,reward,done,_ = env.step(action)
    Throttle = max (Throttle-0.005,0)
    total_reward += reward
    #(x2,y2,p2) = preprocess(next_state)
    #print(action,total_reward,done,x2,y2,p2)
    time.sleep(0.05)
    #if done:
    #    break
print("total reward:",end = '')
print(total_reward)
#env.close()
keyboard.wait()
