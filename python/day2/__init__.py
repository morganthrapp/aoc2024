from python_utils.aoc_utils import get_input


def part_one():
  valid_reports = 0
  def is_safe(report):
    report = list(map(int, report.split()))
    is_ascending = report[0] < report[1]
    for current, next in zip(report, report[1:]):
      if is_ascending and (current >= next):
        return False
      elif not is_ascending and current <= next:
        return False

      if abs(current - next) > 3:
        return False
    return True

  for report in get_input(2):
    valid_reports += 1 if is_safe(report) else 0
  
  return valid_reports

def part_two():
  valid_reports = 0
  def is_subset_safe(report):
    for i in range(len(report)):
      cloned_report = [*report]
      del cloned_report[i]
      if is_safe(cloned_report, False):
        return True
    return False


  def is_safe(report, can_recurse=True):
    is_ascending = report[0] < report[1]
    for i, (current, next) in enumerate(zip(report, report[1:]), 1):
      if is_ascending and (current >= next):
        return can_recurse and is_subset_safe(report)
      elif not is_ascending and current <= next:
        return can_recurse and is_subset_safe(report)

      if abs(current - next) > 3:
        return can_recurse and is_subset_safe(report)
    return True

  for report in get_input(2):
    report = list(map(int, report.split()))
    valid_reports += 1 if is_safe(report) else 0
  
  return valid_reports