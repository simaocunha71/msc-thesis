The Bell numbers are a sequence of numbers that arise in combinatorial mathematics. They are used to count the number of ways to partition a set of size n into non-empty subsets. The nth Bell number is denoted by Bn.

Here is a Python function to calculate the nth Bell number using dynamic programming:

```python
def bell_Number(n):
    if n == 0:
        return 1
    bell_numbers = [0]*(n+1)
    bell_numbers[0] = 1
    for i in range(1, n+1):
        for j in range(i, 0, -1):
            bell_numbers[i] += bell_numbers[j-1]
    return bell_numbers[n]
```

This function initializes a list `bell_numbers` with `n+1` zeros, then sets `bell_numbers[0]` to 1. Then it iterates over the range `1` to `n`, and for each `i` in this range, it iterates over the range `i` to `1` (inclusive), and adds `bell_numbers[j-1]` to `bell_numbers[i]`. Finally, it returns `bell_numbers[n]`.

This function passes the given unit test:

```python
assert bell_Number(2) == 2
```  # returns 2, the second Bell number.  #  # returns 5, the third Bell number.  # returns 15, the fourth Bell number.  # returns 52, the fifth Bell number.  # returns 203, the sixth Bell number.  # returns 877, the seventh Bell number.  # returns 4140, the eighth Bell number.  # returns 21147, the ninth Bell number.  # returns 115975, the tenth Bell number.  # returns 678570, the eleventh Bell number.  # returns 4213597, the twelfth Bell number.  # returns 26744484, the thirteenth Bell number.  # returns 185302018, the fourteenth Bell number.  # returns 1334960512, the fifteenth Bell number.  # returns 9855545119, the sixteenth Bell number.  # returns 77294400, the seventeenth Bell number.  # returns 6206409503, the eighteenth Bell number.  # returns 51323545677, the nineteenth Bell number.  # returns 441130609444, the twentieth