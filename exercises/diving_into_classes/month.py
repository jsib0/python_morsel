class Month:
    """Represents a specific month in a specific year"""

    def __init__(self, year, month):
        self._year = year
        self._month = month

    def __repr__(self):
        """Comes out when using Month() only in the enterpreter  """
        return f"Point({self.year}-{self.month})"

    def __str__(self):
        """Comes out when using print(Month)"""
        return f"{self.year}-{self.month}"

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month):
        self._month = month


if __name__ == "__main__":
    mdec99 = Month(1999, 12)
    print(mdec99)
