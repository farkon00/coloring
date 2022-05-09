import re

from typing import Iterable

class Style:
    def __init__(self, color='white', bold=False, italic=False, underline=False):
        self.color = color
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def generate_string(self, set_colors):
        rgb = re.compile("RGB:\s?\d{1,3},\s?\d{1,3},\s?\d{1,3}")
        output = ''
        if self.bold:
            output += '\033[1m'
        if self.italic:
            output += '\033[3m'
        if self.underline:
            output += '\033[4m'
        if self.color in set_colors:
            color = set_colors[self.color]
            output += '\033[38;2;' + str(color[0]) + ';' + str(color[1]) + ';' + str(color[2]) + 'm'
        elif rgb.match(self.color):
            _, r, g, b = map(lambda x: x.strip(), re.split('[:,]', rgb.match(self.color).group()))
            output += '\033[38;2;' + r + ';' + g + ';' + b + 'm'
        elif isinstance(self.color, Iterable):
            if len(self.color) != 3:
                raise ValueError("Color must be a tuple of length 3")

            output += '\033[38;2;' + str(self.color[0]) + ';' + str(self.color[1]) + ';' + str(self.color[2]) + 'm'

        return output