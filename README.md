# Coloring

![](https://img.shields.io/github/commit-activity/m/morrigan-plus-plus/coloring)![](https://img.shields.io/badge/Current%20Status-Under%20Development-red)

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

Use `clear()` to simply clear the console:

```python
color.clear()
```
