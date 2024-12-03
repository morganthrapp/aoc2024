import datetime
import importlib

from python_utils.aoc_utils import get_input

for day in range(1, datetime.datetime.now().day + 1):
  try:
    module = importlib.import_module(f'day{day}')
  except ModuleNotFoundError as e:
    print(f'Day {day} has not been implemented yet')
    print(e)
    continue

  data = get_input(day)
  
  print(f'Day {day} - Part 1: {module.part_one(data)}')
  try:
    part_two = module.part_two
  except AttributeError:
    print(f'Day {day} Part 2 not implemented yet')
    continue

  print(f'Day {day} - Part 2: {module.part_two(data)}')
  
