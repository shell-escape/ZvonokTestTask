from collections import defaultdict
from typing import Iterable


def get_stats(data: Iterable[str]) -> dict[str, list[int]]:
    """Get stats of employees as dictionary {name: list of hours per day}.

    Args:
        data: iterable of strings; Number after last space is
        concidered as hours.

    >>> get_stats(['Андрей 9', 'X Æ A-12 45', 'Андрей 6'])
    {'Андрей': [9, 6], 'X Æ A-12': [45]}
    """
    stats = defaultdict(list)
    for line in data:
        name, hours = line.rsplit(" ", 1)
        stats[name].append(int(hours))
    return dict(stats)


def print_stats(stats: dict[str, list[int]]) -> None:
    """Prints stat for each employee."""
    for name, hours_list in stats.items():
        print(f"{name}: {str(hours_list)[1:-1]}; sum: {sum(hours_list)}")


if __name__ == "__main__":
    with open("./task2_data.txt", "r") as f:
        try:
            print_stats(get_stats(f))
        except ValueError:
            print(
                "Incorrect data format. Make sure the data includes the "
                "employee's name and number of hours, separated by a space."
            )
