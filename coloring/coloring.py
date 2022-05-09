import re

class Coloring:
    """
    A class to color and style text
    """

    set_colors = {
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
    Print some text with a specific style
    
    Arguments:
        text: The text to be printed and styled
        style: An (optional) style string to dictate how the text will be styled
    Returns:
        Nothing
    """
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
            else:
                color_set = False
                for key in self.set_colors.keys():
                    if key in style:
                        color_set = True
                        color = self.set_colors[key]
                        output += '\033[38;2;' + str(color[0]) + ';' + str(color[1]) + ';' + str(color[2]) + 'm'
            print(output + text + escape)
