To solve this problem, we can use the built-in JavaScript function `match()` to find all the occurrences of the `substring` in the `string`. The `match()` function returns an array of the matches, so we can simply get the length of this array to determine how many times the `substring` appears in the `string`.

Here's the code to solve the problem:

```javascript
const howManyTimes = (string, substring) => {
  return string.match(new RegExp(substring, 'g')).length;
};
```

In this code, we use the `RegExp` constructor to create a regular expression object that matches the `substring`. The `'g'` flag is used to perform a global search, which means that all matches should be returned, even if they overlap. The `length` property of the array returned by `match()` gives us the number of matches, which is the number of times the `substring` appears in the `string`.

For example, if we call `howManyTimes('aaa', 'a')`, the `substring` 'a' appears 3 times in the string 'aaa', so the function returns 3.

Similarly, if we call `howManyTimes('aaaa', 'aa')`, the `substring` 'aa' appears 3 times in the string 'aaaa', so the function returns 3.

Finally, if we call `howManyTimes('', 'a')`, there are no matches because the `substring` 'a' does not appear in an empty string, so the function returns 0.

I hope this helps you solve the problem! Let me know if you have any further questions.
```

```python
def howManyTimes(string, substring):
    return len(string.split(substring))
```

This Python solution works by splitting the original string into a list of substrings at every occurrence of the given substring. The length of the resulting list is then returned as the number of times the substring appears in the original string, including overlapping cases.

For example, if we call `howManyTimes('aaa', 'a')`, the string 'aaa' is split into a list of substrings at every occurrence of 'a', which are ['a', 'a', '