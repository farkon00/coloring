from coloring import Coloring

color = Coloring()

color.clear()

color.setCursor(10, 20)

color.print("Hello, green world!", "RGB: 0, 255, 0")
color.print("Using a set color!", "red")
color.print("Italic, and blue!", "italic underline lightblue")
color.print("Strikethrough and underline", "strikethrough underline")
