def _is_leap(day: int, year: int) -> bool:
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        else:
            if year % 400 == 0:
                return True
    return False


def check(tha_date: str) -> bool:
    low_y_lim = 1
    hi_y_limit = 9999
    low_m_lim = 1
    hi_m_lim = 12
    low_d_lim = 1
    hi_d_lim = 0
    day, month, year = list(map(int, tha_date.split(".")))

    if low_y_lim > year or year > hi_y_limit:
        return False

    if low_m_lim > month or month > hi_m_lim:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:
        hi_d_lim = 31
    elif month == 2:
        if _is_leap(day, year):
            hi_d_lim = 29
        else: hi_d_lim = 28
    else: hi_d_lim = 30

    if low_d_lim > day or day > hi_d_lim:
        return False

    return True