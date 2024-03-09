from functools import cached_property
from typing import Final

from attrs import define, field


@define
class URLBundle:
    filename: Final[str] = field()
    year: Final[int] = field()
    month: Final[int] = field()
    day: Final[int] = field()
    hour: Final[int] = field()
    minute: Final[int] = field()
    second: Final[int] = field()
    millisecond: Final[int] = field()
    live: bool | None = field(default=None)

    @cached_property
    def url(self) -> str:
        return f"https://downloadcenter.samsung.com/content/FM/{self.year:04d}{self.month:02d}/{self.year:04d}{self.month:02d}{self.day:02d}{self.hour:02d}{self.minute:02d}{self.second:02d}{self.millisecond:03d}/{self.filename}"
