from coloring import Coloring, Style

color = Coloring()

color.clear()

color.print("Hello, green world!", Style((233, 255, 0), ["bold", "italic"]))
color.print("Using a set color!", "red")
color.print("Italic, and blue!", "italic underline lightblue")
color.print("Strikethrough and underline", "strikethrough underline")