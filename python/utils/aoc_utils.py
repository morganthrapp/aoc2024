from collections.abc import Iterator


def get_input(day: int) -> list[str]:
    with open(f"inputs/day{day}", "r") as input_data:
        return input_data.readlines()


def stream_input(day: int) -> Iterator[str]:
    with open(f"inputs/day{day}", "r") as input_data:
        while line := input_data.readline():
            yield line


def get_item(data, x, y, x_adjustment, y_adjustment, column_count, row_count):
    adjusted_x = x + x_adjustment
    adjusted_y = y + y_adjustment
    if not (0 <= adjusted_x <= column_count) or not (0 <= adjusted_y <= row_count):
        raise IndexError()
    return data[adjusted_y][adjusted_x]
