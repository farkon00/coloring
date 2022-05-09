import re

class Coloring:
    """
    A class to color and style text
    """

    def __init__(self):
        pass

    def print(self, text, style=None):
        if style == None:
            print(text)
        else:
            output = ''
            escape = '\033[0m'
            # Colors
            rgb = re.compile("RGB:\s?\d{1,3},\s?\d{1,3},\s?\d{1,3}")
            rgbMatch = rgb.match(style)
            if rgbMatch:
                [placeholder, r, g, b] = map(lambda x: x.strip(), re.split('[:,]', rgbMatch.group()))
                output += '\033[38;2;' + r + ';' + g + ';' + b + 'm'
            print(output + text + escape)
