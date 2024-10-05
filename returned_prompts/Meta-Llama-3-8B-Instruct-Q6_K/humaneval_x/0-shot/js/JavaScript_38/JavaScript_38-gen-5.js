```
const decodeCyclic = (s) => {
  let result = '';
  for (let i = 0; i < s.length; i += 3) {
    if (i + 3 <= s.length) {
      result += s.slice(i + 2, i + 3) + s.slice(i, i + 2);
    } else {
      result += s.slice(i);
    }
  }
  return result;
};
```


In the `encodeCyclic` function, we first group the input string into groups of three characters. If a group has less than three characters, it is added as is. For groups with three characters, we cycle the last character to the front. The groups are then joined together to form the encoded string.

The `decodeCyclic` function reverses this process. It iterates over the encoded string in groups of three characters. If a group has three characters, it reorders them to their original order. If a group has less than three characters, it is added as is. The decoded groups are then joined together to form the original string.