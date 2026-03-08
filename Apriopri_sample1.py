from itertools import combinations

transactions = [
    {"burger","fries","cola"},
    {"burger","cola"},
    {"fries","cola"},
    {"burger","fries"},
    {"burger","fries","cola"},
]

min_support = 2

# collect all unique items
items = set()
for t in transactions:
    items.update(t)

frequent = {}

# check combinations up to 3 items
for r in range(1,4):
    for combo in combinations(items,r):

        count = 0
        for t in transactions:
            if set(combo).issubset(t):
                count += 1

        if count >= min_support:
            frequent[combo] = count

print("Frequent itemsets:")
for k,v in frequent.items():
    print(k,"->",v)