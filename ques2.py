from typing import List, Optional

def earliest_trilogy_year(titles: List[str], years: List[int]) -> Optional[int]:
    """
    Returns the earliest year in which a trilogy of books was published, or None if no such trilogy exists.

    Args:
    titles (List[str]): A list of book titles.
    years (List[int]): A list of corresponding publication years.

    Returns:
    Optional[int]: The earliest year in which a trilogy of books was published, or None if no such trilogy exists.
    """
    if len(years) < 3:
        return None

    for i in range(len(years)-2):
        if years[i+2] == years[i+1]+1 == years[i]+2:
            return years[i]

    return None

titles = ['Book1', 'Book2', 'Book3', 'Book4', 'Book5', 'Book6']
years = [2019, 2021, 2012, 2013, 2016, 2017]
print(earliest_trilogy_year(titles, years))
# Output: None

titles = ['Book1', 'Book2', 'Book3', 'Book4', 'Book5', 'Book6']
years = [2019, 2021, 2012, 2013, 2014, 2015]
print(earliest_trilogy_year(titles, years))