import os


def clear_screen() -> None:
    """
    Clears the console screen.

    This function uses the 'os' module to determine the current operating system and # noqa E501
    clears the console screen using the appropriate command for that system.

    Args:
    None.

    Returns:
    None.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
