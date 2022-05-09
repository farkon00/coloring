import re

class Style:
    def __init__(self, color='white', formatting=None):
        self.color = color
        self.formatting = formatting if formatting is not None else []

    def _set_formatting(self, formatting, value):
        if value:
            if formatting not in self.formatting:
                self.formatting.append(formatting)
        else:
            self.formatting.remove(formatting)

    def set_bold(self, value): self._set_formatting('bold', value)
    def set_italic(self, value): self._set_formatting('italic', value)
    def set_underline(self, value): self._set_formatting('underline', value)
    def set_strikethrough(self, value): self._set_formatting('strikethrough', value)

    def generate_string(self, set_colors, formatting):
        rgb = re.compile("RGB:\s?\d{1,3},\s?\d{1,3},\s?\d{1,3}")
        output = ''
        for form in self.formatting:
            if form not in formatting:
                raise ValueError("Unknown formatting: " + str(form))
            output += formatting[form]

        if self.color in set_colors:
            color = set_colors[self.color]
            output += '\033[38;2;' + str(color[0]) + ';' + str(color[1]) + ';' + str(color[2]) + 'm'
        elif isinstance(self.color, tuple | list):
            if len(self.color) != 3:
                raise ValueError("Color must be a tuple of length 3")

            output += '\033[38;2;' + str(self.color[0]) + ';' + str(self.color[1]) + ';' + str(self.color[2]) + 'm'
        elif rgb.match(self.color):
            _, r, g, b = map(lambda x: x.strip(), re.split('[:,]', rgb.match(self.color).group()))
            output += '\033[38;2;' + r + ';' + g + ';' + b + 'm'

        return output