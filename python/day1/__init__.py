from python_utils.aoc_utils import get_input
from itertools import groupby

def build_data():
  first = []
  second = []
  for line in get_input(1):
    f, s = line.split()
    first.append(int(f))
    second.append(int(s))

  first.sort()
  second.sort()
  return first, second

def part_one():
  total = 0

  first, second = build_data()

  for f, s in zip(first, second):
    total += abs(f - s)

  return total

def part_two():
  total = 0
  first, second = build_data()

  second_counts = {k: len(list(g)) for k, g in groupby(second)}

  for num in first:
    total += (num * second_counts.get(num, 0))

  return total