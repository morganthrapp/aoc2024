import itertools

from utils.aoc_utils import get_item


def part_one(data):
    data = list(map(lambda r: r.strip(), data))
    xmas_coords = set()
    x = 0
    y = 0
    column_count = len(data[0]) - 1
    row_count = len(data) - 1
    while y <= row_count:
        if data[y][x] == "X":
            for x_adjustment, y_adjustment in itertools.product([-1, 0, 1], repeat=2):
                try:
                    for i, l in enumerate("MAS", 1):
                        if not (
                            get_item(
                                data,
                                x,
                                y,
                                x_adjustment * i,
                                y_adjustment * i,
                                column_count,
                                row_count,
                            )
                            == l
                        ):
                            raise IndexError()
                    xmas_coords.add(f"{y},{x}-{y_adjustment,x_adjustment}")
                except:
                    pass
        if x < column_count:
            x += 1
        else:
            x = 0
            y += 1

    return len(xmas_coords)


def part_two(data):
    data = list(map(lambda r: r.strip(), data))
    xmas_coords = set()
    x = 0
    y = 0
    column_count = len(data[0]) - 1
    row_count = len(data) - 1
    while y <= row_count:
        if data[y][x] == "A":
            try:
                if (
                    sum(
                        [
                            (
                                get_item(data, x, y, -1, -1, column_count, row_count)
                                == "M"
                                and get_item(data, x, y, 1, 1, column_count, row_count)
                                == "S"
                            ),
                            (
                                get_item(data, x, y, 1, -1, column_count, row_count)
                                == "S"
                                and get_item(data, x, y, -1, 1, column_count, row_count)
                                == "M"
                            ),
                            (
                                get_item(data, x, y, -1, -1, column_count, row_count)
                                == "S"
                                and get_item(data, x, y, 1, 1, column_count, row_count)
                                == "M"
                            ),
                            (
                                get_item(data, x, y, 1, -1, column_count, row_count)
                                == "M"
                                and get_item(data, x, y, -1, 1, column_count, row_count)
                                == "S"
                            ),
                        ]
                    )
                    == 2
                ):

                    xmas_coords.add(f"{y},{x}")
            except IndexError:
                pass
        if x < column_count:
            x += 1
        else:
            x = 0
            y += 1

    return len(xmas_coords)
