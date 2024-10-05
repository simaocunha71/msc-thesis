```js
const encodeCyclic = (s) => {
  let groups = [], groups2 = [];
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
  let groups = [], groups2 = [];
  for (let i = 0; i < Math.floor((s.length + 2) / 3); i++) {
    groups.push(s.slice(3 * i, Math.min((3 * i + 3), s.length)));
  }
  for (const group of groups) {
    if (group.length == 3)
      groups2.push(group.slice(-1) + group.slice(0, -1));
    else
      groups2.push(group);
  }
  return groups2.join('');
}
```

The `decodeCyclic` function takes as input a string encoded with the `encodeCyclic` function and returns the decoded string. It works by reversing the process of the `encodeCyclic` function. For each group of three characters, it moves the last character to the front. If the group has less than three characters, it leaves it unchanged. Finally, it joins all the groups together to form the decoded string.