Here is a solution:

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
}

const decodeCyclic = (s) => {
  var groups = [], groups2 = [];
  for (let i = 0; i < Math.floor((s.length + 2) / 3); i++) {
    groups.push(s.slice(3 * i, Math.min((3 * i + 3), s.length)));
  }
  for (const group of groups) {
    if (group.length == 3)
      groups2.push(group[2] + group.slice(0, 2));
    else
      groups2.push(group);
  }
  return groups2.join('');
}
```

The `encodeCyclic` function splits the string into groups of three characters. If a group has three characters, it moves the first character to the end of the group. If a group has less than three characters, it leaves it as is. Finally, it joins all the groups together into a single string.

The `decodeCyclic` function does the opposite of the `encodeCyclic` function. It splits the string into groups of three characters. If a group has three characters, it moves the last character to the beginning of the group. If a group has less than three characters, it leaves it as is. Finally, it joins all the groups together into a single string.