Here is the solution:
```
const encodeCyclic = (s) => {
  let groups = [];
  for (let i = 0; i < Math.floor((s.length + 2) / 3); i++) {
    groups.push(s.slice(3 * i, Math.min((3 * i + 3), s.length)));
  }
  let result = [];
  for (const group of groups) {
    if (group.length == 3) {
      result.push(group[2] + group[1] + group[0]);
    } else {
      result.push(group);
    }
  }
  return result.join('');
};

const decodeCyclic = (s) => {
  let result = [];
  for (let i = 0; i < s.length; i += 3) {
    if (i + 2 < s.length) {
      result.push(s[i + 2] + s[i + 1] + s[i]);
    } else {
      result.push(s.slice(i));
      break;
    }
  }
  return result.join('');
};
```
Here's an explanation of the code:

`encodeCyclic` function:
* It iterates over the input string in groups of 3 characters.
* For each group, it checks if the group has 3 characters. If it does, it rotates the group by 1 character to the left (i.e., moves the first character to the end). If the group has less than 3 characters, it leaves it as is.
* The function returns the encoded string by concatenating all the groups.

`decodeCyclic` function:
* It iterates over the input string in groups of 3 characters.
* For each group, it checks if the group has 3 characters. If it does, it rotates the group back to its original order (i.e., moves the last character to the beginning). If the group has less than 3 characters, it leaves it as is.
* The function returns the decoded string by concatenating all the groups.

Note that the `encodeCyclic` function is not a one-to-one function, meaning that the same input string can produce different output strings depending on the length of the input string. For example, the input string "abc" can produce either "bca" or "abc" depending on whether the group has 3 characters or not. Therefore, the `decodeCyclic` function needs to be careful when decoding the string to ensure that it produces