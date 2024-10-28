  let sum = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i].charCodeAt(0) >= 65 && s[i].charCodeAt(0) <= 90) {
      sum += s[i].charCodeAt(0);
    }
  }
  return sum;
};

console.log(digitSum("")); // 0
console.log(digitSum("abAB")); // 131
console.log(digitSum("abcCd")); // 67
console.log(digitSum("helloE")); // 69
console.log(digitSum("woArBld")); // 131
console.log(digitSum("aAaaaXa")); // 153




/*
Explanation:
The function digitSum takes a string as an argument and initializes a variable sum to zero. It then uses a for loop to iterate through each character of the string. Inside the loop, it checks if the character is an uppercase letter by using the charCodeAt method to get the ASCII code of the character. If the ASCII code is between 65 and 90 (inclusive), it means the character is an uppercase letter, so it adds the ASCII code to the sum. Finally, the function returns the sum.

In the provided examples, the function is called with different strings as arguments, and the resulting sums are logged to the console.

*/































































































































































