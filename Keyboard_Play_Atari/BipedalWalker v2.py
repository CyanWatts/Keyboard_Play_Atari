import gym
import keyboard
import numpy as np
import time
'''
！！！！！！！！！！！！！！Continuous！！！！！！！！！！！！！！！！
Failed 
'''
EPSILON = 1
total_reward = 0
env = gym.make('BipedalWalker-v3')
state = env.reset()
print(env.action_space)
#action = 0
Hip_1 = 0.
Knee_1 = 0.
Hip_2 = 0.
Knee_2 = 0.
def taction(joint, operation):
    if operation == "add":
        joint = min(joint + EPSILON, 1)
    else:
        joint = max (joint - EPSILON, -1)
    return joint

'''

'''

def abc(x):
    #print("abc")
    global Hip_1
    global Hip_2
    global Knee_1
    global Knee_2

    if x.event_type == "down" and x.name == 'w':    #Hip_1 add
        Hip_1 = taction(Hip_1,"add")
    elif x.event_type == "down" and x.name == 'a':  #Knee_1 add
        Knee_1 = taction(Knee_1,"add")
    elif x.event_type == "down" and x.name == 's':  #Hip_1 sub
        Hip_1 = taction(Hip_1,"sub")
    elif x.event_type == "down" and x.name == 'd':  #Knee_1 sub
        Knee_1 = taction(Knee_1,"sub")
    elif x.event_type == "down" and x.name == 'i':  #Hip_2 add
        Hip_2 = taction(Hip_2,"add")
    elif x.event_type == "down" and x.name == 'j':  #Knee_2 add
        Knee_2 = taction(Knee_2,"add")
    elif x.event_type == "down" and x.name == 'k':  #Hip_2 sub
        Hip_2 = taction(Hip_2,"sub")
    elif x.event_type == "down" and x.name == 'l':  #Knee_2 sub
        Knee_2 = taction(Knee_2,"sub")
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
    action = np.array([Hip_1, Knee_1, Hip_2, Knee_2])
    print(action)
    next_state,reward,done,_ = env.step(action)
    total_reward += reward
    #(x2,y2,p2) = preprocess(next_state)
    #print(action,total_reward,done,x2,y2,p2)
    time.sleep(0.2)
    #if done:
    #    break
print("total reward:",end = '')
print(total_reward)
#env.close()
keyboard.wait()
