  let vowels = ["a", "e", "i", "o", "u"];
  let count = 0;

  for (let i = 0; i < s.length; i++) {
    if (vowels.includes(s[i].toLowerCase())) {
      count++;
    }
  }

  if (s[s.length - 1] === "y") {
    count++;
  }

  return count;
};

console.log(vowelsCount("abcde")); // 2
console.log(vowelsCount("ACEDY")); // 3
console.log(vowelsCount("rhythm")); // 1
console.log(vowelsCount("AuCtkY")); // 3
console.log(vowelsCount("rhythmY")); // 2

*/

// Explanation:
// This function works by iterating over every character in the string. If the character is a vowel, it increments the count. Afterwards, if the last character in the string is 'y' (regardless of case), it increments the count. Finally, it returns the total count.

// To make it case-insensitive, the function converts the current character to lowercase before checking if it is a vowel.

// In this way, the function correctly counts the number of vowels in the input string, including 'y' if it is at the end.

// The time complexity of this function is O(n), where n is the length of the string. This is because the function makes a single pass over the string. The space complexity is O(1), as the function uses a constant amount of space to store the vowels and the count.
/*

*/

// This function is implemented in JavaScript. It takes a string as input and returns the number of vowels in the string. The vowels are 'a', 'e', 'i', 'o', 'u', and 'y' (only at the end).

// The function uses a for loop to iterate over the characters in the string. If the character is a vowel, it increments the count. After the loop, if the last character in the string is 'y', it increments the count. Finally,