Here is the solution to the problem:

```javascript
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
  let decoded = '', temp = '';
  for (let i = 0; i < s.length; i++) {
    temp += s[i];
    if ((i + 1) % 3 == 0) {
      decoded += temp[2] + temp[1] + temp[0];
      temp = '';
    }
  }
  if (temp.length > 0)