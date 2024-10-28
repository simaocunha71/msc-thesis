```
const encodeCyclic = (s) => {
  let result = '';
  for (let i = 0; i < s.length; i += 3) {
    if (i + 3 <= s.length) {
      result += s.slice(i + 1, i + 3) + s[i];
    } else {
      result += s.slice(i) + ' ';
    }
  }
  return result.trim();
};

const decodeCyclic = (s) => {
  let result = '';
  for (let i = 0; i < s.length; i += 2) {
    if (i + 2 <= s.length) {
      result += s.slice(i, i + 2) + s[i + 2];
    } else {
      result += s.slice(i);
    }
  }
  return result;
};
```


Explanation:
The encodeCyclic function takes a string as input and encodes it by cycling groups of three characters. The function works by iterating over the input string in groups of three characters. If the group is complete (i.e., it has three characters), it is cycled by moving the first character to the end of the group. If the group is incomplete (i.e., it has less than three characters), it is appended to the result as is.

The decodeCyclic function takes a string as input and decodes it by reversing the encoding process. It works by iterating over the input string in groups of two characters. If the group is complete (i.e., it has two characters), it is decoded by moving the second character to the end of the group. If the group is incomplete (i.e., it has only one character), it is appended to the result as is. The function also handles the case where the input string is not a multiple of three characters by appending the remaining characters to the result. The function returns the decoded string.