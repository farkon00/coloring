import re
import os

from coloring.style import Style

class Coloring:
    """
    A class to color and style text
    """

    formatting = {
        "bold": "\033[1m",
        "italic": "\033[3m",
        "underline": "\033[4m",
        "strikethrough": "\033[9m",
    }

    set_colors = {
        "white" : [255, 255, 255],
        "red": [255, 0, 0],
        "orange": [255, 127, 0],
        "yellow": [255, 255, 0],
        "green": [0, 255, 0],
        "lightblue": [0, 255, 255],
        "blue": [0, 0, 255],
        "purple": [255, 0, 255],
    }

    def __init__(self):
        pass
    """
    Simply clears the console
    """

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    """
    Set the cursor position within the console

    Arguments:
        x: The x position of the cursor
        y: The y position of the cursor
    Returns:
        success: A boolean indicating whether the cursor position was set successfully
    """

    def setCursor(self, x, y):
        if os.name != 'nt':
            print("\033[%d;%dH" % (y, x))
            return True
        else:
            # TODO: Move the cursor on Windows
            return False

    """
    Print some text with a specific style
    
    Arguments:
        text: The text to be printed and styled
        style: An (optional) style string to dictate how the text will be styled
    Returns:
        Nothing
    """
    def print(self, text, style=None):
        escape = '\033[0m'
        if style == None:
            print(text)
            return
        elif isinstance(style, Style):
            output = style.generate_string(self.set_colors)
        else:
            output = ''
            escape = '\033[0m'
            for key in self.formatting.keys():
                if re.search(r"\b" + re.escape(key) + r"\b", style):
                    output += self.formatting[key]

            # Colors
            rgb = re.compile("RGB:\s?\d{1,3},\s?\d{1,3},\s?\d{1,3}")
            rgbMatch = rgb.match(style)
            if rgbMatch:
                [placeholder, r, g, b] = map(lambda x: x.strip(), re.split('[:,]', rgbMatch.group()))
                output += '\033[38;2;' + r + ';' + g + ';' + b + 'm'
            else:
                color_set = False
                for key in self.set_colors.keys():
                    if re.search(r"\b" + re.escape(key) + r"\b", style):
                        color = self.set_colors[key]
                        output += '\033[38;2;' + str(color[0]) + ';' + str(color[1]) + ';' + str(color[2]) + 'm'
        print(output + text + escape)
