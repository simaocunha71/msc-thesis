```
const splitWords = (txt) => {
  let result = txt.split(' ');
  if (!result.length) {
    result = txt.split(',');
  }
  if (!result.length) {
    let count = 0;
    for (let i = 0; i < txt.length; i++) {
      if (txt[i].toLowerCase() >= 'a' && txt[i].toLowerCase() <= 'z' && (i % 2 !== 0)) {
        count++;
      }
    }
    return count;
  }
  return result;
};
```


Explanation:
The function takes a string `txt` as input. It first tries to split the string on whitespace using the `split()` method. If the resulting array is empty, it means there are no whitespaces in the string, so it tries to split on commas.

If the string still doesn't contain any whitespaces or commas, it means the string only contains letters. In this case, the function counts the number of lower-case letters with odd order in the alphabet. It does this by iterating over the string and checking if each character is a lower-case letter and if its index is odd. If both conditions are true, it increments the count.

Finally, the function returns the result. If the string was split on whitespace or commas, it returns the resulting array. If the string was counted, it returns the count of lower-case letters with odd order in the alphabet.