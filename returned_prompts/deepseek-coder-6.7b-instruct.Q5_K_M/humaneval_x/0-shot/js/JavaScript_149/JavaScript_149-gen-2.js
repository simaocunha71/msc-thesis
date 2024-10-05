  let evenLengthStrings = lst.filter(str => str.length % 2 === 0);
  evenLengthStrings.sort((a, b) => a.length - b.length || a.localeCompare(b));
  return evenLengthStrings;
}

console.log(sortedListSum(["aa", "a", "aaa"]))
console.log(sortedListSum(["ab", "a", "aaa", "cd"]))

// The function first filters the list to only include strings with even length,
// then it sorts the list first by the length of the string, and then by alphabetical order.
// The result is a list sorted by both length and alphabetical order.
```

### Expected Output:

```
["aa"]
["ab", "cd"]
```

## Test Cases:

```python
assert list_sort(["aa", "a", "aaa"]) == ["aa"]
assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
```

## Solution:

```python
def list_sort(lst):
    evenLengthStrings = [str for str in lst if len(str) % 2 == 0]
    evenLengthStrings.sort(key=lambda s: (len(s), s))
    return evenLengthStrings

print(list_sort(["aa", "a", "aaa"]))
print(list_sort(["ab", "a", "aaa", "cd"]))
```

## Expected Output:

```
['aa']
['ab', 'cd']
```

## Test Cases:

```python
assert list_sort(["aa", "a", "aaa"]) == ["aa"]
assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
```

## Solution:

```python
def list_sort(lst):
    evenLengthStrings = [str for str in lst if len(str) % 2 == 0]
    evenLengthStrings.sort(key=lambda s: (len(s),