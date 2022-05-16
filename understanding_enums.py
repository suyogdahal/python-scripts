from enum import Enum, unique, auto


@unique
class DaysOfWeek(Enum):
    """
    DaysOfWeek
    this is enums for days of week
    """

    Monday = auto()
    Tuesday = auto()
    Wednesday = auto()
    Thursday = auto()
    Friday = auto()
    Saturday = auto()
    Sunday = auto()


if __name__ == "__main__":
    print(DaysOfWeek.Monday.name)
    print(DaysOfWeek.Monday.value)

    for day in DaysOfWeek:
        print(day.value)
