from .terminal.helpers import ascii_out, linebreak, out, Position


def print_startup_message():
    ascii_out("Company Admin")
    linebreak(5)
    out("This is test", Position.CENTER)
