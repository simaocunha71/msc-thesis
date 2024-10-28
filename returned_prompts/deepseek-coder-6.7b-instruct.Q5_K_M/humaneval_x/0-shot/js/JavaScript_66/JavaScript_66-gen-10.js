  let sum = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === s[i].toUpperCase() && isNaN(s[i])) {
      sum += s[i].charCodeAt();
    }
  }
  return sum;
}

console.log(digitSum("abAB")); // 131
console.log(digitSum("abcCd")); // 67
console.log(digitSum("helloE")); // 69
console.log(digitSum("woArBld")); // 131
console.log(digitSum("aAaaaXa")); // 153
console.log(digitSum("")); // 0

//  This function works by looping over each character in the string. 
// If the character is an uppercase letter and not a digit, its ASCII value is added to the sum. 
// Finally, the sum is returned.


//  The charCodeAt() method is used to get the ASCII value of a character. 
// The isNaN() function is used to check if a character is not a digit.

//  The function is case-sensitive and does not consider digits as uppercase letters.

//  If the string is empty, the function returns 0 as expected.
//  If all characters in the string are uppercase letters, the function returns the sum of their ASCII values.
//  If there are lowercase letters in the string, they are ignored.
//  If there are digits in the string, they are also ignored.
//  If there are no uppercase letters in the string, the function returns 0.
//  If there are uppercase letters and digits in the string, the function returns the sum of the ASCII values of the uppercase letters only.
















































































