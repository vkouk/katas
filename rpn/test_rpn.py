import pytest
import rpn


def test_split():
    str = '1 2 3 +'
    assert rpn.splitStr(str) == ['1', '2', '3', '+']
    str2 = '3 5 + 6 8 - 1 /'
    assert rpn.splitStr(str2) == ['3', '5', '+', '6', '8', '-', '1', '/']
    with pytest.raises(Exception):
        rpn.splitStr(True)


def test_rpn_calculation():
    str = '1 2 + 3 +'
    assert rpn.rpn_calculation(str) == 6
    str2 = '2 5 + 1 - 3 / 2 -'
    assert rpn.rpn_calculation(str2) == 0
    str3 = '2 2 * 10 * 15 + 5 - 10 /'
    assert rpn.rpn_calculation(str3) == 5
    str4 = '81 SQRT'
    assert rpn.rpn_calculation(str4) == 9
    str5 = '1 2 40 90 280 102 150 250 MAX'
    assert rpn.rpn_calculation(str5) == 280
    with pytest.raises(Exception):
        rpn.rpn_calculation(True)
