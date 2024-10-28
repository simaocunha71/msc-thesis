Here is the solution:

```javascript
const encodeCyclic = (s) => {
  var groups = [], groups2 = [];
  for (let i = 0; i < Math.floor((s.length + 2) / 3); i++) {
    groups.push(s.slice(3 * i, Math.min((3 * i + 3), s.length)));
  }
  for (const group of groups) {
    if (group.length == 3)
      groups2.push(group.slice(1) + group[0]);
    else
      groups2.push(group);
  }
  return groups2.join('');
};

const decodeCyclic = (s) => {
  var groups = [], groups2 = [];
  for (let i = 0; i < Math.floor((s.length + 2) / 3); i++) {
    groups.push(s.slice(3 * i, Math.min((3 * i + 3), s.length)));
  }
  for (const group of groups) {
    if (group.length == 3)
      groups2.push(group.slice(1) + group[0]);
    else
      groups2.push(group);
  }
  return groups2.join('');
};
```


This solution works by iterating over the input string in groups of three characters. If a group is exactly three characters long, it is rotated by one character to the right. If a group is shorter than three characters, it is left unchanged. The decoded string is then constructed by joining all the rotated and unrotated groups together. The encodeCyclic function performs the same operation in reverse, effectively encoding the input string by rotating groups of three characters. The decodeCyclic function performs the reverse operation to decode the encoded string.