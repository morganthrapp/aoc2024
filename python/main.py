import os
import datetime
import importlib

from python_utils.aoc_utils import get_input

def write_answer_file(day, part, answer):
  file_path = f'./answers/{day}-{part}' 
  if not os.path.exists('./answers'):
    os.makedirs('./answers')
  if not os.path.exists(file_path):
    with open(file_path, 'w') as answer_file:
      answer_file.write(str(answer))


for day in range(1, datetime.datetime.now().day + 1):
  try:
    module = importlib.import_module(f'day{day}')
  except ModuleNotFoundError as e:
    print(f'Day {day} has not been implemented yet')
    print(e)
    continue

  data = get_input(day)
  
  part_one_answer = module.part_one(data)

  write_answer_file(day, 1, part_one_answer)

  print(f'Day {day} - Part 1: {part_one_answer}')
  try:
    part_two = module.part_two
  except AttributeError:
    print(f'Day {day} Part 2 not implemented yet')
    continue

  part_two_answer = module.part_two(data)

  write_answer_file(day, 2, part_two_answer)

  print(f'Day {day} - Part 2: {part_two_answer}')

  
