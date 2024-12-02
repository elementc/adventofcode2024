#!/usr/bin/env python3
import sys

left_list = []
right_list = []
lines = sys.stdin.readlines()
for line in lines:
    left, right = line.split()
    left_list.append(int(left))
    right_list.append(int(right))

left_list.sort()
right_list.sort()

total_distance = 0
for i in range(len(left_list)):
    total_distance += abs(left_list[i] - right_list[i])
print(total_distance)
