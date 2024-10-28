You can solve this problem by rotating the second word and checking if it is a substring of the first word. Here is the code:

```javascript
const cycpatternCheck = (a, b) => {
  const n = b.length;
  for (let i = 0; i < n; i++) {
    const rotated = b.slice(i) + b.slice(0, i);
    if (a.includes(rotated)) {
      return true;
    }
  }
  return false;
};

console.log(cycpatternCheck("abcd","abd")); // false
console.log(cycpatternCheck("hello","ell")); // true
console.log(cycpatternCheck("whassup","psus")); // false
console.log(cycpatternCheck("abab","baa")); // true
console.log(cycpatternCheck("efef","eeff")); // false
console.log(cycpatternCheck("himenss","simen")); // true
```