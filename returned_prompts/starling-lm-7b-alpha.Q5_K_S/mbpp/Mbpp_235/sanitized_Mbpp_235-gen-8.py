from future_builtins import *
import sys
import math
import os
from io import BytesIO, IOBase
def even_bit_set_number(n):
    return n | (n << 1)