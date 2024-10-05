```
const encodeCyclic = (s) => {
  const groups = [];
  for (let i = 0; i < Math.floor((s.length + 2) / 3); i++) {
    const group = s.slice(3 * i, Math.min((3 * i + 3), s.length));
    if (group.length === 3) {
      groups.push(group.slice(1) + group[0]);
    } else {
      groups.push(group);
    }
  }
  return groups.join('');
};

const decodeCyclic = (s) => {
  let decoded = '';
  for (let i = 0; i < s.length; i += 3) {
    const group = s.slice(i, i + 3);
    if (group.length === 2) {
      decoded += group[0] + group[1];
    } else {
      decoded += group;
    }
  }
  return decoded;
};
```


Here is how it works:

In the encodeCyclic function, we first split the input string into groups of three characters each. If the group has three characters, we rotate the group by moving the first character to the end of the group. If the group has less than three characters, we leave it as it is. Then we join all the groups together into a single string and return it.

In the decodeCyclic function, we do the opposite of what the encodeCyclic function does. We split the input string into groups of three characters each. If the group has two characters, we rotate the group by moving the first character to the end of the group. If the group has three characters, we leave it as it is. Then we join all the groups together into a single string and return it.

This way, the encodeCyclic function encodes the string by rotating groups of three characters, and the decodeCyclic function decodes the string by rotating the groups back to their original order.