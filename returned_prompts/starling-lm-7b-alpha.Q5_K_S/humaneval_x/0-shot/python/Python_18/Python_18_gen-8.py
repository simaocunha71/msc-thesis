
Here's a simple solution that uses the count() method of the string class:

```python
def how_many_times(string: str, substring: str) -> int:
    return string.count(substring)
```

Here's a more optimized solution that uses a sliding window to count occurrences of the substring, which has a time complexity of O(n) (linear) instead of O(n * m) (where m is the length of the substring):

```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    index = 0
    while index < len(string):
        if string[index] == substring[0]:
            if all(string[i] == substring[i] for i in range(len(substring))):
                count += 1
            index += 1
        else:
            index = max(index + 1, index + len(substring) - 1)
    return count
```

To test the function, you can use the doctest module:

```python
from doctest import TEST_MATCH

tests = r"""
>>> how_many_times('', 'a')
0
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
>>> how_many_times('aaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaxaaaxaxaaaxaxaaaxaxaaaxaxaaaxaxaaxaxaaaxaaxaaaxaxaaaaxaxaaiaaxaxaaiaaxaaiaaxaaiaoaiaaxaaiaaoiaaaiaoaiaiaiaiaaoiaoaiaaiacaoaiacaoiaocaiacaoiaocaiacaoiaocaiacaoaiacaoiaociaaoiaociaaoiaocaiacaoiaocaiaociaocaiacaoiaacaoiaiaacaoiaaoicrnaiaocnaicrnaicaoicnaiaociaocnaiaocnaiaocraicnoiaicnaia