Here's a possible solution:

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
      groups2.push(group.slice(-1) + group.slice(0, -1));
    else
      groups2.push(group);
  }
  return groups2.join('');
}
```

In the `encodeCyclic` function, we first split the input string into groups of three characters using a `for` loop and the `slice` method. Then, we cycle the characters in each group by slicing and concatenating the string. Finally, we join all the groups together and return the result.

In the `decodeCyclic` function, we do the reverse operation. We split the input string into groups of three characters and then un-cycle the characters in each group by slicing and concatenating the string. Finally, we join all the groups together and return the result.