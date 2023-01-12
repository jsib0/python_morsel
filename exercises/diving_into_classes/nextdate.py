from datetime import date, timedelta
from enum import IntEnum


class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class NextDate:
    """Given the next weekday, calculates the days until the given day."""

    def __init__(self, next_weekday):
        self.next_weekday = next_weekday

    def date(self):
        """Returns next weekday's date"""
        today = date.today()
        return today + timedelta((self.next_weekday - today.weekday()) % 7)

    def days_until(self):
        """days until given next weekday"""
        return (self.date() - date.today()).days
