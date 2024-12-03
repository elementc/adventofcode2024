#!/usr/bin/env python3
import re
import sys

memory = sys.stdin.read()

matcher = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

instructions = re.findall(matcher, memory)

acc = 0
for instr in instructions:
  acc += ( int(instr[0]) * int(instr[1]))

print(acc)
