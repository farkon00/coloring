"""Main module in coloring package."""

import os

from coloring.style import Style

class Coloring:
    """
    A class to color and style text
    """

    formatting: dict[str, str] = {
        "bold": "\033[1m",
        "italic": "\033[3m",
        "underline": "\033[4m",
        "strikethrough": "\033[9m",
        "overline" : "\033[53m",
        "doubleunderline" : "\033[21m",
    }

    set_colors: dict[str, tuple[int, int, int]] = {
        "white" : (255, 255, 255),
        "red": (255, 0, 0),
        "orange": (255, 127, 0),
        "yellow": (255, 255, 0),
        "green": (0, 255, 0),
        "lightblue": (0, 255, 255),
        "blue": (0, 0, 255),
        "purple": (255, 0, 255),
    }

    def clear(self) -> None:
        """
        Simply clears the console
        """
        os.system('cls' if os.name == 'nt' else 'clear')


    def set_cursor(self, x: int, y: int) -> bool:
        """
        Set the cursor position within the console

        Arguments:
            x: The x position of the cursor
            y: The y position of the cursor
        Returns:
            success: A boolean indicating whether the cursor position was set successfully
        """
        if os.name != 'nt':
            print(f"\033[{y};{x}H")
            return True

        # TODO: Move the cursor on Windows
        return False

    def print(self, text: str, style: str | Style | None = None) -> None:
        """
        Print some text with a specific style

        Arguments:
            text: The text to be printed and styled
            style: An (optional) style string to dictate how the text will be styled or Style object
        Returns:
            Nothing
        """
        escape = '\033[0m'
        if not style:
            print(text)
            return

        if isinstance(style, Style):
            output = style.generate_string(self.set_colors, self.formatting)
        elif isinstance(style, str):
            output = Style.from_string(style, self.set_colors, self.formatting).\
                generate_string(self.set_colors, self.formatting)

        print(output + text + escape)
