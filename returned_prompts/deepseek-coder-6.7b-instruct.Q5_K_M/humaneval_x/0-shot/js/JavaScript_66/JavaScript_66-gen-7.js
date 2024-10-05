  let sum = 0;
  for (let i = 0; i < s.length; i++) {
    let code = s.charCodeAt(i);
    if (code >= 65 && code <= 90) {
      sum += code;
    }
  }
  return sum;
}

// Test cases
console.log(digitSum("")); // 0
console.log(digitSum("abAB")); // 131
console.log(digitSum("abcCd")); // 67
console.log(digitSum("helloE")); // 69
console.log(digitSum("woArBld")); // 131
console.log(digitSum("aAaaaXa")); // 153

// charCodeAt(i) returns the Unicode of the character at index i in the string.
// Ascii values of uppercase letters range from 65 to 90.
// We loop through the string and if the character's Unicode is within the uppercase range, we add it to our sum.
// Finally we return the sum.

// In the test cases, we see that the function correctly calculates the sum of the ASCII values of uppercase characters in the strings.

// This function can be used to create a simple Caesar cipher, as it will work on strings and can be easily adapted to other tasks.

// The function uses a loop to iterate over each character in the string. For each character, it gets the ASCII value using the charCodeAt() method. If the ASCII value is within the range of uppercase letters (65-90), it is added to the sum. The function then returns the sum.

// The function is case sensitive, so it will only count uppercase letters. If you want to count both uppercase and lowercase letters, you would need to add an additional condition to check if the ASCII value is within the range of lowercase letters (97-122).

// In summary, this function is a simple way to calculate the sum of the ASCII values of uppercase letters in a string.

// The time complexity of this function is O(n), where n is the length of the string. This is because we are loop