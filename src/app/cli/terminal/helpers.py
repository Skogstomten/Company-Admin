from enum import Enum
from os import system, get_terminal_size
from pyfiglet import print_figlet


class Position(Enum):
    CENTER = "center"
    LEFT = "left"


def clear() -> None:
    system("cls")


def ascii_out(text: str, position: Position = Position.CENTER) -> None:
    print_figlet(text, justify=position.value, width=get_terminal_size().columns)


def linebreak(number_of: int = 1) -> None:
    print("\n" * number_of)


def out(text: str, position: Position = Position.LEFT) -> None:
    match position:
        case Position.CENTER:
            text = text.center(get_terminal_size().columns)

    print(text)
