from coloring import Coloring, Style

color = Coloring()

color.clear()

color.print("Hello, world!", Style((233, 255, 0), bg_color="RGB:23,56,3", formatting=["bold", "italic"]))
color.print("Using a a string style!", "BG:78,0,45")
color.print("Italic, and blue!", "italic underline lightblue")
color.print("Strikethrough and underline", "strikethrough underline")