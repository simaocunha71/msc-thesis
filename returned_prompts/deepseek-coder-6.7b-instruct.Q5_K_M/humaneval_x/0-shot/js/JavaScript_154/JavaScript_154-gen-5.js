  const len = b.length;
  
  for (let i = 0; i < len; i++) {
    if (a.includes(b)) return true;
    b = b.slice(len-1) + b.slice(0, len-1);
  }
  
  return false;
}

console.log(cycpatternCheck("abcd","abd")); // false
console.log(cycpatternCheck("hello","ell")); // true
console.log(cycpatternCheck("whassup","psus")); // false
console.log(cycpatternCheck("abab","baa")); // true
console.log(cycpatternCheck("efef","eeff")); // false
console.log(cycpatternCheck("himenss","simen")); // true

// This solution works by checking if the second word or any of its rotations is a substring in the first word. 
// It uses a for loop to rotate the second word and checks if it is a substring of the first word, if it is, it returns true. 
// If no rotation is a substring of the first word, it returns false after checking all rotations.
// The time complexity of this solution is O(n*m) where n is the length of the first word and m is the length of the second word.
// The space complexity of this solution is O(n) where n is the length of the first word.
// This solution assumes that the input words are all lowercase and do not contain any special characters.

// Test cases:
// - "abcd", "abd" => false
// - "hello", "ell" => true
// - "whassup", "psus" => false
// - "abab", "baa" => true
// - "efef", "eeff" => false
// - "himenss", "simen" => true
// All test cases pass.

// P.S. The solution assumes that the input words are all lowercase and do not contain any special characters.
// If the words can contain uppercase letters, special characters, or spaces, the solution would need to be modified to handle those cases.
// This solution also assumes that the rotations are circular, meaning that the last character of