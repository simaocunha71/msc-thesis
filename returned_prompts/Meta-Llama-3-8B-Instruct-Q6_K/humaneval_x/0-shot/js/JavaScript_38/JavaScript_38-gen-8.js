Here is the implementation of the `encodeCyclic` and `decodeCyclic` functions:

```javascript
const encodeCyclic = (s) => {
  let groups = [];
  for (let i = 0; i < Math.floor((s.length + 2) / 3); i++) {
    let group = s.slice(3 * i, Math.min((3 * i + 3), s.length));
    if (group.length == 3) {
      groups.push(group.slice(1) + group[0]);
    } else {
      groups.push(group);
    }
  }
  return groups.join('');
}

const decodeCyclic = (s) => {
  let decoded = '';
  for (let i = 0; i < s.length; i += 3) {
    let group = s.slice(i, i + 3);
    if (group[0] == group[2]) {
      decoded += group[0] + group[1];
    } else {
      decoded += group;
    }
  }
  return decoded;
}
```

The `encodeCyclic` function groups the input string into groups of three characters. If a group has exactly three characters, it reverses the group. The function then joins the groups into a single string.

The `decodeCyclic` function takes a string encoded with `encodeCyclic` and decodes it. It iterates over the input string in groups of three characters. If the first and third characters of a group are the same, it replaces the group with the first character and the second character. Otherwise, it leaves the group unchanged. The function then returns the decoded string.