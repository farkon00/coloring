"""
Module containing the Style class.
"""

import re

class Style:
    """Class representing style of string for Coloring class."""

    def __init__(self, color: tuple[int, int, int] | str = "white",
     bg_color: tuple[int, int, int] | str = "",
     formatting: None | list[str] = None) -> None:
        self.color = color
        self.bg_color = bg_color
        self.formatting = formatting if formatting is not None else []

    def _set_formatting(self, formatting: str, value: bool) -> None:
        if value:
            if formatting not in self.formatting:
                self.formatting.append(formatting)
        else:
            self.formatting.remove(formatting)

    def set_bold(self, value: bool) -> None: self._set_formatting('bold', value)
    def set_italic(self, value: bool) -> None: self._set_formatting('italic', value)
    def set_underline(self, value: bool) -> None: self._set_formatting('underline', value)
    def set_strikethrough(self, value: bool) -> None: self._set_formatting('strikethrough', value)

    def generate_string(self, set_colors: dict[str, tuple[int, int, int]],
     formatting: dict[str, str]) -> str:
        """
        Generates ANSI esacape sequence string for the style.
        """

        rgb = re.compile(r"RGB:\s?\d{1,3},\s?\d{1,3},\s?\d{1,3}")
        output = ''
        for form in self.formatting:
            if form not in formatting:
                raise ValueError("Unknown formatting: " + str(form))
            output += formatting[form]

        rgbmatch = None
        if isinstance(self.color, str):
            rgbmatch = rgb.match(self.color)

        if isinstance(self.color, str) and self.color in set_colors:
            color = set_colors[self.color]
            output += '\033[38;2;' + str(color[0]) + ';' + str(color[1]) + ';' + str(color[2]) + 'm'
        elif isinstance(self.color, tuple | list):
            if len(self.color) != 3:
                raise ValueError("Color must be a tuple of length 3")

            output += f'\033[38;2;{self.color[0]};{self.color[1]};{self.color[2]}m'
        elif rgbmatch:
            _, r, g, b = map(lambda x: x.strip(), re.split('[:,]', rgbmatch.group()))
            output += '\033[38;2;' + r + ';' + g + ';' + b + 'm'

        # BG Color
        if isinstance(self.bg_color, str):
            rgbmatch = rgb.match(self.bg_color)
            if rgbmatch:
                _, r, g, b = map(lambda x: x.strip(), re.split('[:,]', rgbmatch.group()))
                output += f"\033[48;2;{r};{g};{b}m"
            elif self.bg_color in set_colors:
                color = set_colors[self.bg_color]
                output += f"\033[48;2;{color[0]};{color[1]};{color[2]}m"
        elif isinstance(self.bg_color, tuple | list):
            if len(self.bg_color) != 3:
                raise ValueError("Background color must be a tuple of length 3")

            output += f"\033[48;2;{self.bg_color[0]};{self.bg_color[1]};{self.bg_color[2]}m"

        return output