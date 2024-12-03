#!/usr/bin/env python3
import re
import sys

memory = sys.stdin.read()

matcher = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)")

instructions = re.findall(matcher, memory)

acc = 0
MODE_RUN = 0
MODE_INHIBIT = 1
mode = MODE_RUN

for instr in instructions:
  if mode == MODE_INHIBIT:
    if instr[2] == "do":
      mode = MODE_RUN

  elif mode == MODE_RUN:
    if instr[2] == "do":
      continue
    elif instr[3] == "don't":
      mode = MODE_INHIBIT
      continue
    acc += ( int(instr[0]) * int(instr[1]))

print(acc)
