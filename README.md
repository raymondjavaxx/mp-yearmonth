# mp-yearmonth

A year-month datatype for Python.

## Installation

```bash
pip install mp-yearmonth
```

## Usage

```python
from mp_yearmonth import YearMonth

ym = YearMonth(2019, 1)
print(ym) # 2019-01
```

Parsing ISO 8601 strings:

```python
ym = YearMonth.parse("2019-01")

print(ym.year) # 2019
print(ym.month) # 1
```

Comparisons:

```python
ym1 = YearMonth(2019, 1)
ym2 = YearMonth(2019, 2)

print(ym1 < ym2) # True
```

Addition:

```python
ym = YearMonth(2019, 1)
ym += 1

print(ym) # 2019-02
```

Range:

```python
ym1 = YearMonth(2019, 1)
ym2 = YearMonth(2019, 3)

for ym in YearMonth.range(ym1, ym2):
    print(ym) # 2019-01, 2019-02, 2019-03
```

## License

mp-yearmonth is licensed under the MIT license. See [LICENSE](LICENSE) for details.
