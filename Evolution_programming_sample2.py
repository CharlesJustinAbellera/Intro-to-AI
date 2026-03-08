# Example 2: Maximizing a Mathematical Function

# Goal: find x that maximizes f(x) = -x² + 10x
# The best solution should be x ≈ 5

import random

population = [random.uniform(0,10) for _ in range(6)]

def fitness(x):
    return -x**2 + 10*x

for generation in range(15):

    offspring = []

    for x in population:
        mutation = x + random.uniform(-1,1)
        offspring.append(mutation)

    population = population + offspring

    population = sorted(population, key=fitness, reverse=True)

    population = population[:6]

best = population[0]

print("Best solution:", best)
print("Maximum value:", fitness(best))