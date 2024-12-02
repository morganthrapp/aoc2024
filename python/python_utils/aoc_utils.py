from collections.abc import Iterator

def get_input(day: int) -> list[str]:
  with open(f'inputs/day{day}', 'r') as input_data:
    return input_data.readlines()

def stream_input(day: int) -> Iterator[str]:
  with open(f'inputs/day{day}', 'r') as input_data:
    while line := input_data.readline():
      yield line