import argparse


def circular_path(n: int, m: int):
    circular_array = list(range(1, n + 1))
    path = []
    start_index = 0

    while True:
        interval = [circular_array[(start_index + i) % n] for i in range(m)]

        path.append(interval[0])

        if interval[-1] == circular_array[0]:
            break

        start_index = (start_index + m - 1) % n

    return path


def main() -> None:
    parser = argparse.ArgumentParser(description='Process circular array parameters.')
    parser.add_argument('n', type=int, help='Length of the circular array')
    parser.add_argument('m', type=int, help='Interval length')

    args = parser.parse_args()
    if not args.n > args.m > 1:
        raise ValueError('Error in parameters')

    path = circular_path(args.n, args.m)

    print(''.join(map(str, path)))


if __name__ == '__main__':
    main()
