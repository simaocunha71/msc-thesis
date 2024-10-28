Here is the solution in JavaScript:

```javascript
const cycpatternCheck = (a, b) => {
  for (let i = 0; i < a.length; i++) {
    for (let j = 0; j <= a.length - b.length; j++) {
      if (a.slice(j, j + b.length).includes(b)) {
        return true;
      }
    }
  }
  for (let i = 0; i < b.length; i++) {
    b = b.slice(i) + b.slice(0, i);
    for (let j = 0; j <= a.length - b.length; j++) {
      if (a.slice(j, j + b.length).includes(b)) {
        return true;
      }
    }
  }
  return false;
};
```

This function works by iterating over the first word and checking if the second word or any of its rotations is a substring. It first checks the second word as is, then it checks all possible rotations of the second word. If it finds a match, it returns true. If it doesn't find a match after checking all possible rotations, it returns false. 

This function has a time complexity of O(n*m), where n is the length of the first word and m is the length of the second word. This is because in the worst case, it needs to iterate over the entire first word for each possible rotation of the second word. 

This function also has a space complexity of O(m), where m is the length of the second word. This is because it needs to store the rotations of the second word in memory. 

This function assumes that the input words are strings and that the second word is not an empty string. It also assumes that the second word is not longer than the first word. If these assumptions are not valid, the function may need to be modified to handle these cases.  */  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  // 