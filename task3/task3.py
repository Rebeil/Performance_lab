import argparse


def read_numbers_from_file(filename: str) -> list[int]:
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers


def min_moves_to_equal_elements(nums: list[int]) -> int | float:
    nums.sort()

    n = len(nums)
    median = nums[n // 2] if n % 2 != 0 else (nums[n // 2 - 1] + nums[n // 2]) // 2

    return sum(abs(num - median) for num in nums)


def main() -> None:
    parser = argparse.ArgumentParser(description='Process file containing numbers.')
    parser.add_argument('filename', type=str, help='The name of the file containing the numbers')

    args = parser.parse_args()
    print(min_moves_to_equal_elements(read_numbers_from_file(args.filename)))


if __name__ == '__main__':
    main()
