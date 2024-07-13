import argparse
import json
from typing import Any


def read_json_file(filename: str) -> dict[str, Any] | list[Any]:
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_json_file(filename: str, data: dict[str, Any] | list[Any]) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def fill_values(tests: list[dict[str, Any]], values_dict: dict[int, str]) -> None:
    for test in tests:
        test_id = test.get('id')
        if test_id is not None and test_id in values_dict:
            test['value'] = values_dict[test_id]

        if 'values' in test:
            fill_values(test['values'], values_dict)


def main() -> None:
    parser = argparse.ArgumentParser(description='Fill test values based on test results.')
    parser.add_argument('values_file', type=str, help='The name of the values JSON file')
    parser.add_argument('tests_file', type=str, help='The name of the tests JSON file')
    parser.add_argument('report_file', type=str, help='The name of the report JSON file')

    args = parser.parse_args()

    values_data = read_json_file(args.values_file)
    tests_data = read_json_file(args.tests_file)

    values_dict = {item['id']: item['value'] for item in values_data['values']}

    fill_values(tests_data['tests'], values_dict)

    write_json_file(args.report_file, tests_data)


if __name__ == '__main__':
    main()
