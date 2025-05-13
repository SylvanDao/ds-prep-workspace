import sys
import os
sys.path.append(os.path.dirname(__file__))

from operations.addition import add
from operations.subtraction import subtract

print(add(2, 3))
print(subtract(5, 1))