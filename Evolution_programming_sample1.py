#Example 1: Minimizing a Mathematical Function

# Goal: find x that minimizes f(x) = (x − 3)²
# The best solution should be x ≈ 3.

import random

population = [random.uniform(-10,10) for _ in range(6)]

def fitness(x):
    return (x-3)**2

for generation in range(15):

    offspring = []

    for x in population:
        mutation = x + random.uniform(-1,1)
        offspring.append(mutation)

    population = population + offspring

    population = sorted(population, key=fitness)

    population = population[:6]

best = population[0]

print("Best solution:", best)
print("Function value:", fitness(best))