import numpy as np
import gym
import matplotlib.pyplot as plt

# Set the learning rate, discount factor, and number of episodes
learning_rate = 0.1
gemma = 0.95
num_episodes = 500

# Crea ambiente.
env = gym.make('FrozenLake-v1')

# Inicializa la tabla Q
Q = np.zeros([env.observation_space.n, env.action_space.n])


for i in range(num_episodes):
    s = env.reset()[0]
    done = False
    episode_reward = 0
    while not done:
        a = np.argmax(Q[s,:] + np.random.randn(1,env.action_space.n)*(1./(i+1)))
        s_, recompensa, done,truncado,info = env.step(a)
        if s_==5:
            recompensa=-1
        if s_==7:
            recompensa=-1
        if s_==11:
            recompensa=-1
        if s_==12:
            recompensa=-1
        Q[s,a] = Q[s,a]+ learning_rate*(recompensa+ num_episodes*np.max(Q[s_,:])-Q[s,a] )
        s=s_

print(recompensa)
print(Q)

env.observation_space



def run(Q):
    env= gym.make("FrozenLake-v1",render_mode="human")
    env.reset()
    s=0
    limite=10
    contador=0
    while contador<limite:
        action= np.argmax(Q[s,:]) 
        #new_state, reward, done, four = env.step(action)
        new_state,reward,done,other,info= env.step(action)
        if done==True:
            observation, info = env.reset()
            s=0
        else:
            s=new_state
    #print(new_state)
    contador=+1
    env.render()
    env.close()

run(Q)
