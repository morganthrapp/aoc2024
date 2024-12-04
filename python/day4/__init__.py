import itertools


def part_one(data):
    def get_item(data, x, y, x_adjustment, y_adjustment, column_count, row_count):
        adjusted_x = x + x_adjustment
        adjusted_y = y + y_adjustment
        if not (0 <= adjusted_x <= column_count) or not (0 <= adjusted_y <= row_count):
            raise IndexError()
        return data[adjusted_y][adjusted_x]

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
                    if (
                        get_item(
                            data,
                            x,
                            y,
                            x_adjustment,
                            y_adjustment,
                            column_count,
                            row_count,
                        )
                        == "M"
                    ):
                        if (
                            get_item(
                                data,
                                x,
                                y,
                                x_adjustment * 2,
                                y_adjustment * 2,
                                column_count,
                                row_count,
                            )
                            == "A"
                        ):
                            if (
                                get_item(
                                    data,
                                    x,
                                    y,
                                    x_adjustment * 3,
                                    y_adjustment * 3,
                                    column_count,
                                    row_count,
                                )
                                == "S"
                            ):
                                xmas_coords.add(f"{y},{x}-{y_adjustment,x_adjustment}")
                except IndexError:
                    pass
        if x < column_count:
            x += 1
        else:
            x = 0
            y += 1

    return len(xmas_coords)


def part_two(data):
    def get_item(data, x, y, x_adjustment, y_adjustment, column_count, row_count):
        adjusted_x = x + x_adjustment
        adjusted_y = y + y_adjustment
        if not (0 <= adjusted_x <= column_count) or not (0 <= adjusted_y <= row_count):
            raise IndexError()
        return data[adjusted_y][adjusted_x]

    data = list(map(lambda r: r.strip(), data))
    xmas_coords = set()
    x = 0
    y = 0
    column_count = len(data[0]) - 1
    row_count = len(data) - 1
    while y <= row_count:
        if data[y][x] == "A":
            try:
                if sum([(
                    get_item(data, x, y, -1, -1, column_count, row_count) == "M"
                    and get_item(data, x, y, 1, 1, column_count, row_count) == "S"
                ) , (
                    get_item(data, x, y, 1, -1, column_count, row_count) == "S"
                    and get_item(data, x, y, -1, 1, column_count, row_count) == "M"
                ) , (
                    get_item(data, x, y, -1, -1, column_count, row_count) == "S"
                    and get_item(data, x, y, 1, 1, column_count, row_count) == "M"
                ) , (
                    get_item(data, x, y, 1, -1, column_count, row_count) == "M"
                    and get_item(data, x, y, -1, 1, column_count, row_count) == "S"
                )]) == 2:

                    xmas_coords.add(f"{y},{x}")
            except IndexError:
                pass
        if x < column_count:
            x += 1
        else:
            x = 0
            y += 1

    return len(xmas_coords)
