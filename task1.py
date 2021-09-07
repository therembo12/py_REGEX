import re

TEST_STRING = """
2006. 05. 04
2006-05-04
2006/05/04
2006-5-4
2006/5/4
4.5.2006
4-5-2006
4/5/2006
04.05.2006
04-05-2006
04/05/2006
"""
year = "2006/12/31"
day = '31/12/2006'
hungary = '2006. 12. 31'


def date_format(data: str):
    day_first_pattern = re.compile(
        r'^(0?[1-9]|[12][0-9]|3[01])[-\.\/](0?[1-9]|1[012])[-\.\/]([0-9]{4})')
    year_first_pattern = re.compile(
        r'([0-9]{4})[-\.\/](0?[1-9]|1[012])[-\.\/](^0?[1-9]|[12][0-9]|3[01])')
    hungary_pattern = re.compile(
        r'([0-9]{4})[.\s]+(0?[1-9]|1[012])[.\s]+(^0?[1-9]|[12][0-9]|3[01])')

    if day_first_pattern.search(data):
        matches = day_first_pattern.search(data)
        day = matches[3]
        month = matches[2]
        year = matches[1]

        return (day, month, year,)
    elif year_first_pattern.search(data):
        matches = year_first_pattern.search(data)
        day = matches[1]
        month = matches[2]
        year = matches[3]

        return (day, month, year,)
    elif hungary_pattern.search(data):
        matches = hungary_pattern.search(data)
        day = matches[1]
        month = matches[2]
        year = matches[3]

        return (day, month, year,)


x = date_format(hungary)
print(x)
