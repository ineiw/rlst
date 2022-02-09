import gym
import numpy as np
import random
import matplotlib.pyplot as plt

env = gym.make('BipedalWalker-v3')
goal_steps = 500

episode=0

while episode < 100:
    obs = env.reset()
    score = 0
    for i in range(goal_steps):
        # env.render()
        obs,reward,done,info = env.step([random.randrange(0,4) for x in range(4)])
        if done:
            break
        score += reward
    episode +=1
    print(f"Episode : {episode} Score : {score}")

obs = env.reset()

for i in range(goal_steps):
        env.render()
        obs,reward,done,info = env.step([random.randrange(0,4) for x in range(4)])
        if done:
            break
env.close()
# pip3 install Box2D
# pip3 install box2d-py
# pip3 install gym[all]
# pip3 install gym[Box_2D]
# pip install pyvirtualdisplay==0.2.*
# pip install gym[all]==0.17.* 
# pip install PyOpenGL==3.1.* PyOpenGL-accelerate==3.1.*