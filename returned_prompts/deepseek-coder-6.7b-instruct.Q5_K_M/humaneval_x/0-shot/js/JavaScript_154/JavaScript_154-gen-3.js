  for (let i = 0; i < b.length; i++) {
    if (a.includes(b)) return true;
    b = b.slice(-1) + b.slice(0, -1);
  }
  return false;
}

console.log(cycpatternCheck("abcd","abd")); // false
console.log(cycpatternCheck("hello","ell")); // true
console.log(cycpatternCheck("whassup","psus")); // false
console.log(cycpatternCheck("abab","baa")); // true
console.log(cycpatternCheck("efef","eeff")); // false
console.log(cycpatternCheck("himenss","simen")); // true

The solution works by looping through all possible rotations of the second string and checking if the first string contains any of the rotations. If any rotation is found, the function returns true; otherwise, it returns false.
*/

function cycpatternCheck(a, b) {
  for (let i = 0; i < b.length; i++) {
    if (a.includes(b)) return true;
    b = b.slice(-1) + b.slice(0, -1);
  }
  return false;
}

console.log(cycpatternCheck("abcd","abd")); // false
console.log(cycpatternCheck("hello","ell")); // true
console.log(cycpatternCheck("whassup","psus")); // false
console.log(cycpatternCheck("abab","baa")); // true
console.log(cycpatternCheck("efef","eeff")); // false
console.log(cycpatternCheck("himenss","simen")); // true

/*
This function works by first checking if the second string is a substring of the first string. If it is, it returns true. If it's not, it then loops through all possible rotations of the second string and checks if any of these rotations are substrings of the first string. If it finds a rotation that is a substring, it returns true. If it doesn't find any rotations that are substrings, it returns false.
*/








