# Coloring

![](https://img.shields.io/github/commit-activity/m/morrigan-plus-plus/coloring)
![](https://img.shields.io/badge/Current%20Status-Under%20Development-red)

__Coloring__ is a simple Python library for printing colored and styled text, with plans to expand to full-fleged TUI library.

## How to use

Simply import Coloring as follows:

```python
from coloring import Coloring
```

Then create a new Coloring object

```python
color = Coloring()
```

Use the `print(text, style)` function to print styled text, for example:

```python
color.print("This text will be purple and underlined", "underline RGB:255, 0, 255")
color.print("This text will also be purple", "purple")
```

Defined styles:

| Style                   | Example        | Output              |
|-------------------------|----------------|---------------------|
| RGB:0-255, 0-255, 0-255 |`RGB:255, 0, 0` | [red]               |
| red / orange / green ...| `green`        | [green]             |
| italic                  | `italic`       | _[italicized]_      |
| strikethrough           | `strikethrough`| ~~[strikethrough]~~ |
| underline               | `underline`    | [underlined]        |
| overline                | `overline`     | [overlined]         |

Availiable colors are : `white, red, orange, yellow, gold, green, lime, aqua, lightblue, blue, magenta, purple, pink`

You can use a style object. It is just a way to write styles in python object. You can change styles over time.
```python
from coloring import Style

color.print("Hello, world!", Style((233, 255, 0), formatting=["bold", "italic", "overline"]))
color.print("Hello, world!", Style((233, 255, 0), bg_color="RGB:23,56,3"))

style = Style()
style.set_bold() # Makes text bold
style.set_italic(True) # Makes text italic
style.set_italic(False) # Makes text not italic
style.color = input("Input color name:") 
color.print("Hi, there!", style)
```

Use `clear()` to simply clear the console:

```python
color.clear()
```

Use `setCursor(x, y)` to set the cursor position on the screen. Currently this really only works in terms of Y position.
And doesnt really work on windows, only unix.

```python
color.setCursor(10, 10)
```
