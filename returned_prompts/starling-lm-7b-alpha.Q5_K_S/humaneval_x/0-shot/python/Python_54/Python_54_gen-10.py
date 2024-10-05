To check if two strings have the same characters, you can sort the characters in each string and compare the sorted strings. If the sorted strings are equal, then the original strings have the same characters. Here's a step-by-step explanation of the solution:

1. Define a function called `same_chars` that takes two string parameters: `s0` and `s1`.
2. Use a `set` to store the unique characters in `s0`. The `set` automatically removes any duplicate characters. For example, if `s0` is "eabcdzzzz", the set would contain {'e', 'a', 'b', 'c', 'z'}.
3. Sort the unique characters in the set using the `sorted` function. This will give you a sorted list of unique characters in `s0`. For example, if `s0` is "eabcdzzzz", the sorted list would be ['a', 'b', 'c', 'd', 'e', 'z', 'z', 'z', 'z'].
4. Repeat steps 2 and 3 for `s1`. This will give you a sorted list of unique characters in `s1`. For example, if `s1` is "dddzzzzzzzddeddabc", the sorted list would be ['a', 'b', 'c', 'd', 'd', 'd', 'd', 'e', 'z', 'z', 'z', 'z', 'z'].
5. Compare the sorted lists of unique characters. If the sorted lists are equal, it means that `s0` and `s1` have the same characters. If the sorted lists are not equal, it means that `s0` and `s1` do not have the same characters.
6. Return `True` if the sorted lists are equal, and `False` otherwise.

Here's the code for the solution:

```python
def same_chars(s0: str, s1: str):
    s0_set = set(s0)
    s0_sorted = sorted(s0_set)
    s1_set = set(s1)
    s1_sorted = sorted(s1_set)
    return s0_sorted == s1_sorted
```

