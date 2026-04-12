import datetime as dm
import os
import pytest as pt

import script_utilities.date as dt

def test_initialisation():
    today = dt.Date()
    
    assert today.year == dm.date.today().year
    assert today.month == dm.date.today().month
    assert today.day == dm.date.today().day

def test_month_zero():
    with pt.raises(ValueError):
        test = dt.Date(2024, 0, 12)

def test_month_one():
    try:
        test = dt.Date(2024, 1, 12)
    except ValueError:
        assert False

def test_month_two():
    try:
        test = dt.Date(2024, 2, 12)
    except ValueError:
        assert False

def test_month_eleven():
    try:
        test = dt.Date(2024, 11, 12)
    except ValueError:
        assert False

def test_month_twelve():
    try:
        test = dt.Date(2024, 12, 12)
    except ValueError:
        assert False

def test_month_thirteen():
    with pt.raises(ValueError):
        test = dt.Date(2024, 13, 12)

def test_day_zero():
    with pt.raises(ValueError):
        test = dt.Date(2024, 1, 0)

def test_day_one():
    try:
        test = dt.Date(2024, 1, 1)
    except ValueError:
        assert False

def test_day_two():
    try:
        test = dt.Date(2024, 1, 2)
    except ValueError:
        assert False

def test_day_thirty():
    try:
        test = dt.Date(2024, 1, 30)
    except ValueError:
        assert False

def test_day_thirthy_one():
    try:
        test = dt.Date(2024, 1, 31)
    except ValueError:
        assert False

def test_day_thirthy_two():
    with pt.raises(ValueError):
        test = dt.Date(2024, 1, 32)

def test_string():
    test = dt.Date(2024, 11, 11)
    assert str(test) == "11-11-2024"

def test_string_day_less_than_ten():
    test = dt.Date(2024, 11, 5)
    assert str(test) == "05-11-2024"

def test_string_month_less_than_ten():
    test = dt.Date(2024, 5, 11)
    assert str(test) == "11-05-2024"

def test_string_both_less_than_ten():
    test = dt.Date(2024, 5, 5)
    assert str(test) == "05-05-2024"

def test_representation():
    test = dt.Date(2024, 5, 3)
    assert repr(test) == "03-05-2024"

def test_addition():
    test = dt.Date(2024, 1, 1)
    test += 40
    assert test == dt.Date(2024, 2, 10)

def test_addition_wrong_type():
    with pt.raises(TypeError):
        test = dt.Date(2024, 5, 12)
        test += "a"

def test_addition_next_month():
    test = dt.Date(2024, 1, 31)
    test += 1
    assert test == dt.Date(2024, 2, 1)

def test_addition_next_year():
    test = dt.Date(2024, 12, 31)
    test += 1
    assert test == dt.Date(2025, 1, 1)

def test_subtraction():
    test = dt.Date(2024, 5, 4)
    test -= 50
    assert test == dt.Date(2024, 3, 15)

def test_subtraction_wrong_type():
    with pt.raises(TypeError):
        test = dt.Date(2024, 3, 4)
        test -= "a"

def test_subtraction_previous_month():
    test = dt.Date(2024, 4, 1)
    test -= 1
    assert test == dt.Date(2024, 3, 31)

def test_subtraction_previous_year():
    test = dt.Date(2024, 1, 1)
    test -= 1
    assert test == dt.Date(2023, 12, 31)

def test_less_than_wrong_type():
    with pt.raises(TypeError):
        test = dt.Date(2024, 4, 15)
        test < 2

def test_less_than_previous():
    test = dt.Date(2024, 7, 29)
    value = test < dt.Date(2024, 7, 28)
    assert not value

def test_less_than_exact():
    test = dt.Date(2024, 7, 29)
    value = test < dt.Date(2024, 7, 29)
    assert not value

def test_less_than_next():
    test = dt.Date(2024, 7, 29)
    value = test < dt.Date(2024, 7, 30)
    assert value

def test_less_than_or_equal_wrong_type():
    with pt.raises(TypeError):
        test = dt.Date(2024, 4, 15)
        test <= "a"

def test_less_than_or_equal_previous():
    test = dt.Date(2024, 7, 29)
    value = test <= dt.Date(2024, 7, 28)
    assert not value

def test_less_than_or_equal_exact():
    test = dt.Date(2024, 7, 29)
    value = test <= dt.Date(2024, 7, 29)
    assert value

def test_less_than_or_equal_next():
    test = dt.Date(2024, 7, 29)
    value = test <= dt.Date(2024, 7, 30)
    assert value

def test_equal_wrong_type():
    with pt.raises(TypeError):
        test = dt.Date(2024, 4, 15)
        test == {2, 3}

def test_equal_previous():
    test = dt.Date(2024, 7, 29)
    value = test == dt.Date(2024, 7, 28)
    assert not value

def test_equal_exact():
    test = dt.Date(2024, 7, 29)
    value = test == dt.Date(2024, 7, 29)
    assert value

def test_equal_next():
    test = dt.Date(2024, 7, 29)
    value = test == dt.Date(2024, 7, 30)
    assert not value

def test_not_equal_wrong_type():
    with pt.raises(TypeError):
        test = dt.Date(2024, 4, 15)
        test != "abc"

def test_not_equal_previous():
    test = dt.Date(2024, 7, 29)
    value = test != dt.Date(2024, 7, 28)
    assert value

def test_not_equal_exact():
    test = dt.Date(2024, 7, 29)
    value = test != dt.Date(2024, 7, 29)
    assert not value

def test_not_equal_next():
    test = dt.Date(2024, 7, 29)
    value = test != dt.Date(2024, 7, 30)
    assert value

def test_greater_than_or_equal_wrong_type():
    with pt.raises(TypeError):
        test = dt.Date(2024, 4, 15)
        test >= {"1": 1}

def test_greater_than_or_equal_previous():
    test = dt.Date(2024, 7, 29)
    value = test >= dt.Date(2024, 7, 28)
    assert value

def test_greater_than_or_equal_exact():
    test = dt.Date(2024, 7, 29)
    value = test >= dt.Date(2024, 7, 29)
    assert value

def test_greater_than_or_equal_next():
    test = dt.Date(2024, 7, 29)
    value = test >= dt.Date(2024, 7, 30)
    assert not value

def test_greater_than_wrong_type():
    with pt.raises(TypeError):
        test = dt.Date(2024, 4, 15)
        test > [1, 2, 3]

def test_greater_than_previous():
    test = dt.Date(2024, 7, 29)
    value = test > dt.Date(2024, 7, 28)
    assert value

def test_greater_than_exact():
    test = dt.Date(2024, 7, 29)
    value = test > dt.Date(2024, 7, 29)
    assert not value

def test_greater_than_next():
    test = dt.Date(2024, 7, 29)
    value = test > dt.Date(2024, 7, 30)
    assert not value

def test_difference():
    test = dt.Date(2024, 5, 16)
    difference = test.difference(dt.Date(2024, 4, 27))
    assert difference == 19

def test_difference_wrong_type():
    with pt.raises(TypeError):
        test = dt.Date(2024, 9, 23)
        test.difference(2)

if __name__ == "__main__":
    os.system(f"pytest {os.path.basename(__file__)}")
