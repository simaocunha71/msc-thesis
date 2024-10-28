  for (let i = 0; i < b.length; i++) {
    if (a.includes(b)) {
      return true;
    }
    b = b.slice(1) + b[0];
  }
  return false;
};

console.log(cycpatternCheck("abcd","abd")); // false
console.log(cycpatternCheck("hello","ell")); // true
console.log(cycpatternCheck("whassup","psus")); // false
console.log(cycpatternCheck("abab","baa")); // true
console.log(cycpatternCheck("efef","eeff")); // false
console.log(cycpatternCheck("himenss","simen")); // true


// The solution works by creating a loop that rotates the second string and checks if it's a substring of the first. It uses the built-in String method 'includes' to check for substrings, and slices and concatenation to rotate the string.

// The time complexity of this solution is O(n*m), where n is the length of the first string and m is the length of the second string. This is because in the worst case, we may need to check all substrings of the first string.

// The space complexity of this solution is O(1), as it only uses a constant amount of space to store the input strings and a counter variable.

// This solution assumes that the input strings are case sensitive and do not contain any special characters. If the strings can be case insensitive, special characters can be ignored, or if the strings can be very long, a more efficient solution would be needed.

// Also, this solution is not efficient for large inputs because it uses the built-in 'includes' method, which has a time complexity of O(n). If a more efficient string searching algorithm is available, it could be used instead.

// In conclusion, this solution is suitable for most use cases, but may not be the most efficient for very large inputs.


// cycpatternCheck("abcd","abd") => false
// cycpatternCheck("hello","ell") => true
// cycpatternCheck("whassup","psus") => false
// cycpatternCheck("abab","baa") => true
// cy