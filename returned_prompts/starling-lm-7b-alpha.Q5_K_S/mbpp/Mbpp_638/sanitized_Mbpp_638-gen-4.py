from math import pow
import math
def wind_chill(T,V):
    return -42.42 + 10.21 * T - 0.25 * V + 0.11 * T * V - 6.12 * (T ** 0.16) - 0.006 * V ** 2