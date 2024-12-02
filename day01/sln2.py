#!/usr/bin/env python3
import sys

left_list = []
right_list = []
lines = sys.stdin.readlines()
for line in lines:
    left, right = line.split()
    left_list.append(int(left))
    right_list.append(int(right))

instance_counts = {}

for item in right_list:
    if item in instance_counts:
        instance_counts[item] = instance_counts[item] + 1
    else:
        instance_counts[item] = 1

similarity_score = 0

for item in left_list:
    if item not in instance_counts:
        continue
    else:
        similarity_score += item * instance_counts[item]

print(similarity_score)
