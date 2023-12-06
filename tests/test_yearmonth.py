import pytest
from mp_yearmonth import YearMonth


def test_init_handles_out_of_range_month():
    with pytest.raises(ValueError, match=r"^month must be between 1 and 12$"):
        YearMonth(2021, 0)

    with pytest.raises(ValueError, match=r"^month must be between 1 and 12$"):
        YearMonth(2021, 13)


def test_init_handles_out_of_range_year():
    with pytest.raises(ValueError, match=r"^year must be between 1 and 9999$"):
        YearMonth(0, 1)

    with pytest.raises(ValueError, match=r"^year must be between 1 and 9999$"):
        YearMonth(10000, 1)


def test_init_handles_non_int_values():
    with pytest.raises(TypeError, match=r"^year must be an integer$"):
        YearMonth("2021", 1)

    with pytest.raises(TypeError, match=r"^month must be an integer$"):
        YearMonth(2021, "1")


def test_str():
    assert str(YearMonth(2021, 1)) == "2021-01"
    assert str(YearMonth(2021, 12)) == "2021-12"
    assert str(YearMonth(100, 1)) == "0100-01"


def test_repr():
    assert repr(YearMonth(2021, 1)) == "YearMonth(2021, 1)"
    assert repr(YearMonth(2021, 12)) == "YearMonth(2021, 12)"


def test_eq():
    assert YearMonth(2021, 1) == YearMonth(2021, 1)
    assert YearMonth(2021, 1) != YearMonth(2021, 2)
    assert YearMonth(2021, 1) != object()


def test_lt():
    assert YearMonth(2021, 1) < YearMonth(2021, 2)
    assert YearMonth(2021, 1) < YearMonth(2022, 1)
    assert not (YearMonth(2021, 1) < YearMonth(2021, 1))
    assert not (YearMonth(2021, 1) < YearMonth(2020, 12))


def test_le():
    assert YearMonth(2021, 1) <= YearMonth(2021, 2)
    assert YearMonth(2021, 1) <= YearMonth(2022, 1)
    assert YearMonth(2021, 1) <= YearMonth(2021, 1)
    assert not (YearMonth(2021, 1) <= YearMonth(2020, 12))


def test_gt():
    assert YearMonth(2021, 2) > YearMonth(2021, 1)
    assert YearMonth(2022, 1) > YearMonth(2021, 1)
    assert not (YearMonth(2021, 1) > YearMonth(2021, 1))
    assert not (YearMonth(2020, 12) > YearMonth(2021, 1))


def test_ge():
    assert YearMonth(2021, 2) >= YearMonth(2021, 1)
    assert YearMonth(2022, 1) >= YearMonth(2021, 1)
    assert YearMonth(2021, 1) >= YearMonth(2021, 1)
    assert not (YearMonth(2020, 12) >= YearMonth(2021, 1))


def test_hash():
    assert hash(YearMonth(2021, 1)) == hash(YearMonth(2021, 1))  # Same
    assert hash(YearMonth(2021, 1)) != hash(YearMonth(2021, 2))  # Different month
    assert hash(YearMonth(2022, 1)) != hash(YearMonth(2021, 1))  # Different year


def test_numdays():
    assert YearMonth(2021, 1).numdays == 31
    assert YearMonth(2021, 2).numdays == 28
    assert YearMonth(2021, 3).numdays == 31
    assert YearMonth(2021, 4).numdays == 30
    assert YearMonth(2021, 5).numdays == 31
    assert YearMonth(2021, 6).numdays == 30
    assert YearMonth(2021, 7).numdays == 31
    assert YearMonth(2021, 8).numdays == 31
    assert YearMonth(2021, 9).numdays == 30
    assert YearMonth(2021, 10).numdays == 31
    assert YearMonth(2021, 11).numdays == 30
    assert YearMonth(2021, 12).numdays == 31

    # Leap year
    assert YearMonth(2020, 2).numdays == 29


def test_current():
    assert YearMonth.current() == YearMonth.parse(str(YearMonth.current()))


def test_parse():
    assert YearMonth.parse("2021-01") == YearMonth(2021, 1)
    assert YearMonth.parse("2021-12") == YearMonth(2021, 12)


def test_parse_handles_invalid_input():
    with pytest.raises(ValueError, match=r"^Invalid YearMonth string format"):
        YearMonth.parse("2021-1")

    with pytest.raises(ValueError, match=r"^Invalid YearMonth string format"):
        YearMonth.parse("21-01")
        assert "Invalid YearMonth string format"

    with pytest.raises(ValueError, match=r"^Invalid YearMonth string format"):
        YearMonth.parse("2021-1a")
        assert "Invalid YearMonth string format"

    with pytest.raises(ValueError, match=r"^Invalid YearMonth string format"):
        YearMonth.parse("2021-01-01")
        assert "Invalid YearMonth string format"

    with pytest.raises(ValueError, match=r"^month must be between 1 and 12$"):
        YearMonth.parse("2021-13")
        assert "Invalid YearMonth string format"


def test_next():
    assert YearMonth(2021, 1).next() == YearMonth(2021, 2)
    assert YearMonth(2021, 12).next() == YearMonth(2022, 1)


def test_range():
    # Ascending
    r = YearMonth.range(YearMonth(2021, 1), YearMonth(2021, 3))
    assert list(r) == [YearMonth(2021, 1), YearMonth(2021, 2), YearMonth(2021, 3)]

    # Descending
    r = YearMonth.range(YearMonth(2021, 3), YearMonth(2021, 1))
    assert list(r) == [YearMonth(2021, 3), YearMonth(2021, 2), YearMonth(2021, 1)]

    # Same
    r = YearMonth.range(YearMonth(2021, 1), YearMonth(2021, 1))
    assert list(r) == [YearMonth(2021, 1)]


def test_applying_delta():
    ym = YearMonth(2021, 1)
    assert ym.applying_delta(0) == YearMonth(2021, 1)
    assert ym.applying_delta(1) == YearMonth(2021, 2)
    assert ym.applying_delta(2) == YearMonth(2021, 3)
    assert ym.applying_delta(3) == YearMonth(2021, 4)
    assert ym.applying_delta(4) == YearMonth(2021, 5)
    assert ym.applying_delta(5) == YearMonth(2021, 6)
    assert ym.applying_delta(6) == YearMonth(2021, 7)
    assert ym.applying_delta(7) == YearMonth(2021, 8)
    assert ym.applying_delta(8) == YearMonth(2021, 9)
    assert ym.applying_delta(9) == YearMonth(2021, 10)
    assert ym.applying_delta(10) == YearMonth(2021, 11)
    assert ym.applying_delta(11) == YearMonth(2021, 12)
    assert ym.applying_delta(12) == YearMonth(2022, 1)

    assert ym.applying_delta(-1) == YearMonth(2020, 12)
    assert ym.applying_delta(-2) == YearMonth(2020, 11)


def test_add():
    ym = YearMonth(2021, 1)
    assert ym + 0 == YearMonth(2021, 1)
    assert ym + 1 == YearMonth(2021, 2)
    assert ym + 2 == YearMonth(2021, 3)


def test_sub():
    ym = YearMonth(2021, 1)
    assert ym - 0 == YearMonth(2021, 1)
    assert ym - 1 == YearMonth(2020, 12)
    assert ym - 2 == YearMonth(2020, 11)
