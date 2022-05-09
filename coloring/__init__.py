"""
A simple Python library for coloring and styling text.
"""

import os

from coloring.style import Style
from coloring.coloring import Coloring

if os.name == 'nt':
    os.system('color')
