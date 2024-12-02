#!/usr/bin/env python3
import sys

records = sys.stdin.readlines()

max_dldr = 3
min_dldr = 1

safe_signals = 0

def filter(record):
  sb_increasing = record[0] < record[1]
  for i in range(len(record) - 1):
    if sb_increasing and not record[i] < record[i+1]:
        print(f"{record} rejected, not increasing {record[i]} -> {record[i+1]}")
        return 0
    if not sb_increasing and not record[i] > record[i+1]:
        print(f"{record} rejected, not decreasing {record[i]} -> {record[i+1]}")
        return 0
    dldr = abs(record[i]-record[i+1])
    if not (min_dldr <= dldr and dldr <= max_dldr):
        print(f"{record} rejected, dldr {dldr} out of bounds {record[i]} -> {record[i+1]}")
        return 0
  return 1
    

for record_str in records:
  record = [int(tok) for tok in record_str.split()]
  safe_signals += filter(record)
print(f"safe records: {safe_signals}")
