import gym
#import time
#env = gym.make('CartPole-v0')
env = gym.make('Breakout-v0')
#print (env.unwrapped.get_action_meanings())

action_dict={}

for i in range(env.action_space.n):
	action_dict[i] = env.unwrapped.get_action_meanings()[i] 



env.reset()

t=0
#print (dir(env))
print (env.action_space.contains)
for _ in range(100):
	t+=1
	#time.sleep(1)

	env.render()
	#input('press any key to start')
	env.env.ale.saveScreenPNG('test_image.png')

	#action =env.action_space.sample()
	print (action_dict)    
	action = int(input('Enter a number from 0 to '+str(env.action_space.n)+':\n'))
	print (action)
	observation, reward, done, info = env.step(action) # take a random action
	

	print ('reward is: ',reward)

	if done:
		print("Episode finished after {} timesteps".format(t+1))
		break
	

#print(c)
env.close()