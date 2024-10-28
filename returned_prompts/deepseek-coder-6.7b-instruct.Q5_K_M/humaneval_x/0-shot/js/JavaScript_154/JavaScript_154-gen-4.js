  const rotate = s => s.slice(1) + s[0];
  for (let i = 0; i < b.length; i++) {
    if (a.includes(b)) return true;
    b = rotate(b);
  }
  return false;
};

console.log(cycpatternCheck("abcd","abd")); // false
console.log(cycpatternCheck("hello","ell")); // true
console.log(cycpatternCheck("whassup","psus")); // true
console.log(cycpatternCheck("abab","baa")); // true
console.log(cycpatternCheck("efef","eeff")); // false
console.log(cycpatternCheck("himenss","simen")); // true

```

The function cycpatternCheck takes two words as parameters. The function rotate is used to rotate the string b in each iteration. If the rotated string b is found in a, the function returns true. If none of the rotations are found, the function returns false.

This function can work with words of any length and will return true if any of the rotations of the second word are substrings of the first word.

The function includes is used to check if a substring is present in a string.

The function slice is used to rotate the string b in each iteration. It takes a substring from the string b starting from the index 1 to the end and adds the first character of the string b to the end.

The function uses a for loop to rotate the string b for as many times as the length of the string b.

The function uses the ternary operator to return true if the rotated string b is found in the string a, and false otherwise.

The function uses the includes method to check if the rotated string b is a substring of the string a.

The function uses the slice method to rotate the string b.
```















































































