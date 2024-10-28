```
const sameChars = (s0, s1) => {
  return s0.split('').sort().join('') === s1.split('').sort().join('');
};
```


Explanation:
The function `sameChars` checks if two strings `s0` and `s1` have the same characters. It does this by first converting each string into an array of characters using `split('')`. Then, it sorts these arrays using `sort()` and joins them back into strings using `join('')`. If the resulting strings are equal, then the original strings have the same characters.

For example, when you call `sameChars('eabcdzzzz', 'dddzzzzzzzddeddabc')`, the function first converts the strings into arrays of characters:

`['e', 'a', 'b', 'c', 'd', 'z', 'z', 'z']` and
`['d', 'd', 'z', 'z', 'z', 'z', 'z', 'd', 'd', 'e', 'd', 'd', 'a', 'b', 'c']`

Then, it sorts these arrays and joins them back into strings:

`'aaabccdddzzz'` and `'aaabccdddzzz'`

Since these strings are equal, the function returns `true`. If the strings are not equal, it returns `false`. This way, you can check if two words have the same characters.