"""
Module containing the Style class.
"""
from __future__ import annotations
from typing import List, Dict, Tuple

import re

Color = Tuple[int, int, int]

class Style:
    """Class representing style of string for Coloring class."""

    RE_RGB = re.compile(r"RGB:\s?\d{1,3},\s?\d{1,3},\s?\d{1,3}")
    RE_BG = re.compile(r"BG:\s?\d{1,3},\s?\d{1,3},\s?\d{1,3}")

    def __init__(self, color: Color | str = "white",
     bg_color: Color | str = "",
     formatting: None | List[str] = None) -> None:
        self.color: Color | str = color
        self.bg_color: Color | str = bg_color
        self.formatting: List[str] = formatting if formatting is not None else []

    def _set_formatting(self, formatting: str, value: bool) -> None:
        if value:
            if formatting not in self.formatting:
                self.formatting.append(formatting)
        else:
            self.formatting.remove(formatting)

    def set_bold(self, value: bool = True) -> None: self._set_formatting('bold', value)
    def set_italic(self, value: bool = True) -> None: self._set_formatting('italic', value)
    def set_underline(self, value: bool = True) -> None: self._set_formatting('underline', value)
    def set_strikethrough(self, value: bool = True) -> None: self._set_formatting('strikethrough', value)

    def generate_string(self, set_colors: Dict[str, Color],
     formatting: Dict[str, str]) -> str:
        """
        Generates ANSI esacape sequence string for the style.
        """

        output = ''
        for form in self.formatting:
            if form not in formatting:
                raise ValueError("Unknown formatting: " + str(form))
            output += formatting[form]

        rgbmatch = None
        if isinstance(self.color, str):
            rgbmatch = self.RE_RGB.match(self.color)

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
            rgbmatch = self.RE_RGB.match(self.bg_color)
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

    @classmethod
    def from_string(cls, style: str, set_colors: Dict[str, Color],
     formatting: Dict[str, str]) -> Style:
        """
        Creates a Style object from a string.
        """
        output = cls()

        for form in formatting:
            if re.search(r"\b" + re.escape(form) + r"\b", style):
                output.formatting.append(form)

        # Colors
        rgb_match = cls.RE_RGB.match(style)
        bg_match = cls.RE_BG.match(style)
        if rgb_match:
            _, r, g, b = map(lambda x: x.strip(), re.split('[:,]', rgb_match.group()))
            output.color = (int(r), int(g), int(b))
        else:
            for key, color in set_colors.items():
                if re.search(r"\b" + re.escape(key) + r"\b", style):
                    output.color = color

        # Bg Color
        if bg_match:
            _, r, g, b = map(lambda x: x.strip(), re.split('[:,]', bg_match.group()))
            output.bg_color = (int(r), int(g), int(b))

        return output
