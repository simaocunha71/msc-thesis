"""
Write a function to find the closest smaller number than n.
assert closest_num(11) == 10
"""
from typing import Optional, List

def closest_num(n: int) -> float:
    def get_closest(cur_num: int) -> float:
        min_val = min(n - cur_num, n + cur_num)
        max_val = max(n - cur_num, n + cur_num)
        return abs((min_val-max_val)/2.0*1e9).lround()
    return get_closest(n//2.0+1)*1e-9

def main():
    print("The smallest number in the range [%d, %d] is: %.6f" % (n // 2 + 1, n, closest_num(n)))

if __name__ == '__main__':
    main()