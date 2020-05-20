import numpy
import GA3
import matplotlib.pyplot as plt
from testpid import testpid
import gym

# Number of the weights we are looking to optimize.
num_weights = 6

sol_per_pop = 24
num_parents_mating = 2

# Defining the population size.
pop_size = (sol_per_pop,num_weights) # The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
#Creating the initial population.
new_population = numpy.random.uniform(low=-1.0, high=1.0, size=pop_size)



#Elöző GA eredmények
new_population[0,:]=[-0.71405516, -0.2312352,  -2.90342396 ,-1.26405387, -0.1265466, -6.95823982]  # fitness: 118
new_population[1,:]=[-0.65833561, -0.19961153, -2.66589629, -1.39491965, -0.10063901,   -7.21695438]  # fitness: 119
new_population[2,:]=[-0.71405516, -0.2312352,  -2.90342396, -1.26405387, -0.1265466,   -6.95823982]  # fitness: 116

# Ebből számaztatt véletlen egyed
for i in range(3,sol_per_pop-2):
	new_population[i,0]=numpy.random.uniform(low=-0.72, high=-0.70)
	new_population[i,1]=numpy.random.uniform(low=-0.24, high=-0.22)
	new_population[i,2]=numpy.random.uniform(low=-3.0, high=-2.8)
	new_population[i,3]=numpy.random.uniform(low=-1.28, high=-1.24)
	new_population[i,4]=numpy.random.uniform(low=-0.14, high=-0.10)
	new_population[i,5]=numpy.random.uniform(low=-7.0, high=-6.8)
	
# Eddigiek átlaga

new_population[sol_per_pop-1,0]=numpy.average(new_population[:,0].reshape(1,sol_per_pop))
new_population[sol_per_pop-1,1]=numpy.average(new_population[:,1].reshape(1,sol_per_pop))
new_population[sol_per_pop-1,2]=numpy.average(new_population[:,2].reshape(1,sol_per_pop))
new_population[sol_per_pop-1,3]=numpy.average(new_population[:,3].reshape(1,sol_per_pop))
new_population[sol_per_pop-1,4]=numpy.average(new_population[:,4].reshape(1,sol_per_pop))
new_population[sol_per_pop-1,5]=numpy.average(new_population[:,5].reshape(1,sol_per_pop))

	
print(new_population)

num_generations = 70


for generation in range(num_generations):
	print("Generation : ", generation)
	# Measing the fitness of each chromosome in the population.
	fitness = GA3.cal_pop_fitness(new_population,generation)

	# Selecting the best parents in the population for mating.
	parents = GA3.select_mating_pool(new_population, fitness, num_parents_mating)

	# Generating next generation using crossover.
	offspring_crossover = GA3.crossover(parents, offspring_size=(pop_size[0]-parents.shape[0], num_weights))
	#print(offspring_crossover)
	
	# Adding some variations to the offsrping using mutation.
	offspring_mutation = GA3.mutation(offspring_crossover)
	#print(offspring_mutation)
	
	# Creating the new population based on the parents and offspring.
	new_population[0:parents.shape[0], :] = parents
	new_population[parents.shape[0]:, :] = offspring_mutation
	
	# The best result in the current iteration.
	#print("Best result : ", numpy.min(fitness))
	#print("Best result : ", numpy.min(GA3.cal_pop_fitness(new_population,generation)))


# Getting the best solution after iterating finishing all generations.
#At first, the fitness is calculated for each solution in the final generation.
fitness = GA3.cal_pop_fitness(new_population,num_generations)
# Then return the index of that solution corresponding to the best fitness.
best_match_idx = numpy.where(fitness == numpy.min(fitness))

if isinstance(best_match_idx, list):
	best_match_idx = best_match_idx[0]

print("Best solution : ", new_population[best_match_idx, :])
print("Best solution fitness : ", fitness[best_match_idx])

testpid(new_population[best_match_idx, :][0][0])
