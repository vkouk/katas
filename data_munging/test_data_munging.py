import pytest
import data_munging


def test_split_lines():
    input = "aa\nbb\n\n\n\ndd\n"
    result = ["bb"]
    assert data_munging.split_lines(input) == result
    input2 = ""
    result2 = []
    assert data_munging.split_lines(input2) == result2
    input3 = "Dy\nMxT\n\nMnt\n"
    result3 = ['MxT']
    assert data_munging.split_lines(input3) == result3


def test_data_row():
    input = "1 20 5  45 90"
    result = {'Dy': 1, 'Mxt': 20, 'MnT': 5}
    assert data_munging.data_row(input) == result
    input2 = "2 45 20/  45 90"
    result2 = {'Dy': 2, 'Mxt': 45, 'MnT': 20}
    assert data_munging.data_row(input2) == result2
    input3 = "3 7 2  45 90"
    result3 = {'Dy': 3, 'Mxt': 7, 'MnT': 2}
    assert data_munging.data_row(input3) == result3
