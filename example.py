from coloring import Coloring, Style

color = Coloring()

color.clear()

color.print("Hello, green world!", Style("RGB: 32, 255, 89", True))
color.print("Using a set color!", "red")
color.print("Underlined, and blue!", "underline lightblue")
