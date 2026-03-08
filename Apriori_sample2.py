#Example 2: Apriori for School Supply Purchases

from itertools import combinations

transactions = [
    {"notebook","pen","eraser"},
    {"notebook","pen"},
    {"pen","pencil"},
    {"notebook","pencil","eraser"},
    {"notebook","pen","pencil"}
]

min_support = 2

items = set()
for t in transactions:
    items.update(t)

frequent_sets = {}

for size in range(1,3):
    for combo in combinations(items,size):

        count = 0
        for t in transactions:
            if set(combo).issubset(t):
                count += 1

        if count >= min_support:
            frequent_sets[combo] = count

print("Frequent item combinations:")
for k,v in frequent_sets.items():
    print(k,"->",v)