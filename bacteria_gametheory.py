import matplotlib.pyplot as plt
import numpy as np 
import math
#import ggplot


base_nutrition = float(100)
base_antibiotic = float(60)

penetrance_nutrition = float(10)
penetrance_antibiotic = float(2.5)

signal_cost = float(5)

death_cost = float(100)

threshold = float(15)


## only one of them should be 1
no_signaling = 1
early_signaling = 0
threshold_signaling = 0


## only one of them should be 1
no_termination = 0
early_termination = 0
threshold_termination = 1


health_inner = []
health_outer = []
steps = []
layers = []
game_on = []
game_flag = 1

epsilon = 0.1

i = 1
for step in range(1,40):

	inner_net = base_nutrition*math.exp(-i/float(penetrance_nutrition)) - base_antibiotic*math.exp(-i/float(penetrance_antibiotic))

	if inner_net > threshold:
		phi = 0
		psi = 0
	if inner_net <threshold and threshold_termination == 0:
		phi = -death_cost
		psi = -death_cost
		game_flag = 0

	if no_signaling == 1:
		signaling = 0

	if early_signaling == 1:
		if inner_net <= threshold*2:
			signaling = -signal_cost
		else:
			signaling =0

	if threshold_signaling == 1:
		if inner_net > threshold:
			signaling = 0
		else:
			signaling = -signal_cost
			epsilon = 0

	if early_termination == 1:
		if inner_net <= threshold*2:
			i -= 1
			epsilon = 0
			game_flag = 0

	if threshold_termination == 1:
		if inner_net <= threshold:
			i -= 1
			epsilon = 0
			game_flag = 0


	print(signaling)
	health_inner.append(base_nutrition*math.exp(-i/penetrance_nutrition) - base_antibiotic*math.exp(-i/penetrance_antibiotic) + signaling + phi)

	health_outer.append(base_nutrition - base_antibiotic*(1-epsilon)  + psi)

	steps.append(step)

	layers.append(i)

	game_on.append(game_flag)
	i += 1

utility_outer = []
utility_inner = []
utility_steps = []

for j in range(1,len(health_inner)-1):
	if game_on[j] == 1:
		utility_inner.append(health_inner[j+1] - health_inner[j])
		utility_outer.append(health_outer[j+1] - health_outer[j])
		utility_steps.append(j)	



plt.plot(utility_steps, utility_inner, color = (31/255., 119/255., 180/255.), label = 'inner')
plt.plot(utility_steps, utility_outer, color = (255/255., 127/255., 14/255.), label = 'outer')
#plt.ylim(0,70)
plt.xlim(0,20)
plt.xlabel("Time")
plt.ylabel("Health")
plt.minorticks_on()
plt.legend()
plt.grid(which = 'major', color = "#D3D3D3", linestyle = '-', linewidth = 0.5)
plt.grid(which = 'minor', color = "#F1F1F1", linestyle = '-')
#plt.grid(b=True, which='major', color='#999999', linestyle='-')
plt.show()
