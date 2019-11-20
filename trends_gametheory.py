import matplotlib.pyplot as plt
import numpy as np 
import math

base_nutrition = float(100)
base_antibiotic = float(60)

penetrance_nutrition = float(10)
penetrance_antibiotic = float(2.5)

signal_cost = float(5)

death_cost = float(100)

threshold = float(15)

time_of_death = []


for penetrance_nutrition in range(1,30):
	i=1
	for step in range(1,200):

		inner_net = base_nutrition*math.exp(-i/float(penetrance_nutrition)) - base_antibiotic*math.exp(-i/float(penetrance_antibiotic))

		if inner_net<threshold:
			time_of_death.append(i)
			break;
		i+=1
		#print(inner_net)


plt.plot(range(1,30), time_of_death)
plt.xlabel("Nutrition penetrance")
plt.ylabel("Optimal number of layers")
plt.show()

