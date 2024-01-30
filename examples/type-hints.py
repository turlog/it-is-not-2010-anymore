from re import Pattern
from typing import Callable, TypeVar

ParsedValue = TypeVar("ParsedValue")


def parse(
    payload: str, pattern: Pattern, parser: Callable[[str], ParsedValue]
) -> ParsedValue | None:
    if (match := pattern.search(payload)) is not None:
        return parser(match.group(0))
    return 0


print(parse("dvdscndwcw123sdasnbdjsd", "[0-9]+", int))
