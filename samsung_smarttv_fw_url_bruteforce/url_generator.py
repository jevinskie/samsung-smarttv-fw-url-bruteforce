from collections.abc import Generator

from .url_bundle import URLBundle

# example:
# https://downloadcenter.samsung.com/content/FM/202402/20240215101137008/T-KTSUAKUC.zip
# YYYYMM/YYYYMMDDHHMMSSsss/FILENAME
# 20240215101137008 => 2024-02-15-10-11-37-008
# 20150126112516169 => 2015-01-26-11-25-16-169
# 20150114175506400 => 2015-01-14-17-55-06-400
# 20150126155809276 => 2015-01-26-15-58-09-276


def num_url_bundles(month: int | None = None) -> int:
    num: int = 1 if month is not None else 12  # months
    num *= 31  # days
    num *= 24  # hours
    num *= 60  # minutes
    num *= 60  # seconds
    num *= 1000  # milliseconds
    return num


def generate_url_bundles(
    filename: str, year: int, month: int | None = None
) -> Generator[URLBundle, None, None]:
    if month is None:
        for _month in range(1, 13):
            for day in range(1, 32):
                for hour in range(24):
                    for minute in range(60):
                        for second in range(60):
                            for millisecond in range(1000):
                                yield URLBundle(
                                    filename,
                                    year,
                                    _month,
                                    day,
                                    hour,
                                    minute,
                                    second,
                                    millisecond,
                                )
    else:
        for day in range(1, 32):
            for hour in range(24):
                for minute in range(60):
                    for second in range(60):
                        for millisecond in range(1000):
                            yield URLBundle(
                                filename,
                                year,
                                month,
                                day,
                                hour,
                                minute,
                                second,
                                millisecond,
                            )
