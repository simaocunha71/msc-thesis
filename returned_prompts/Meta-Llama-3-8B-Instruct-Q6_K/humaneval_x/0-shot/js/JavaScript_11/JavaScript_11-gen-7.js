```
  let result = '';
  let i = 0;
  while (i < a.length && i < b.length) {
    if (a[i] === b[i]) {
      result += '0';
    } else {
      result += '1';
    }
    i++;
  }
  return result;
}
```


Explanation:
The function takes two binary strings as input and performs a bitwise XOR operation on them. The result is then converted back to a string. The XOR operation is performed by iterating over the characters of both strings, and for each pair of characters, if they are the same, the result is '0', otherwise it is '1'. The result is then returned as a string. 

For example, if the input strings are '010' and '110', the function will return '100', which is the result of the XOR operation on the two input strings. 

The time complexity of this function is O(n), where n is the length of the input strings, because it iterates over the characters of both strings once. The space complexity is O(n), because in the worst case, the result string can be as long as the input strings. 





