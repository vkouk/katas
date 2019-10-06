file = open('weather.dat', 'r')


def split_lines(lines):
    line = lines.splitlines()
    filteredLines = list(filter(lambda l: l != '', line))
    newLines = []
    if len(filteredLines) > 2:
        newLines = filteredLines[1:2]
    return newLines


def data_row(row):
    dataObj = {
        'Dy': int(row[:1]),
        'Mxt': int(row[2:4]),
        'MnT': int(row[4:7])
    }
    return dataObj


def smallest_spread_temperature():
    print('weather')


def weather():
    print('weather')
