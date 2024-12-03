from python_utils.aoc_utils import get_input
import re


def part_one():
  instructions = ''.join(get_input(3))
  matcher = re.compile('mul\\((\\d{1,3}),(\\d{1,3})\\)')
  muls = matcher.findall(instructions)
  total = 0
  for match in muls:
    a, b = match
    total += (int(a) * int(b))
    
  return total

def part_two():
  instructions = ''.join(get_input(3))
  matcher = re.compile("(?:mul\\((\\d{1,3}),(\\d{1,3})\\)|(do\\(\\))|(don't\\(\\)))")
  muls = matcher.findall(instructions)
  total = 0
  active = True
  for match in muls:
    a, b, do, do_not = match
    if active and a and b:
      total += (int(a) * int(b))
    if do:
      active = True
    if do_not:
      active = False
    
  return total