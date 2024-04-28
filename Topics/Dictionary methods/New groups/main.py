from itertools import zip_longest

# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
group_sizes = []

groups_to_fill = int(input())

for _ in range(groups_to_fill):
    group_sizes.append(int(input()))

groups_and_sizes = list(zip_longest(groups, group_sizes))

print(dict(groups_and_sizes))
