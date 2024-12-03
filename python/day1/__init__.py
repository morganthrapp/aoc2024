from itertools import groupby

def build_data(data):
  first = []
  second = []
  for line in data:
    f, s = line.split()
    first.append(int(f))
    second.append(int(s))

  first.sort()
  second.sort()
  return first, second

def part_one(data):
  total = 0

  first, second = build_data(data)

  for f, s in zip(first, second):
    total += abs(f - s)

  return total

def part_two(data):
  total = 0
  first, second = build_data(data)

  second_counts = {k: len(list(g)) for k, g in groupby(second)}

  for num in first:
    total += (num * second_counts.get(num, 0))

  return total