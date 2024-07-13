import math
import argparse
from typing import Iterator, Tuple


def read_file(filename: str) -> str:
    with open(filename, 'r') as file:
        content = file.read()
    return content


def parse_content_to_pairs(content: str) -> Iterator[Tuple[int, int]]:
    for line in content.splitlines():
        x, y = map(int, line.split())
        yield x, y


def is_point_outside_circle(x: int, y: int, x_c: int, y_c: int) -> float:
    return math.sqrt((x - x_c) ** 2 + (y - y_c) ** 2)


def main() -> None:
    parser = argparse.ArgumentParser(description='Read two name files')
    parser.add_argument('circle_file', type=str, help='The name of the circle txt file')
    parser.add_argument('dot_file', type=str, help='The name of the dot txt file')

    args = parser.parse_args()
    circle_coordinates = read_file(args.circle_file).splitlines()

    x_c, y_c = map(int, circle_coordinates[0].split())  # Координаты центра окружности
    r = int(circle_coordinates[1])  # Радиус окружности

    for x, y in parse_content_to_pairs(read_file(args.dot_file)):
        distance = is_point_outside_circle(x, y, x_c, y_c)
        if distance > r:
            print(2)
        elif distance == r:
            print(0)
        elif distance < r:
            print(1)


if __name__ == '__main__':
    main()
