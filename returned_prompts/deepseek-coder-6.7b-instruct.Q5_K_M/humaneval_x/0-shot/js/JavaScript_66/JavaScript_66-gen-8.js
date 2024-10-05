  let sum = 0;
  for(let i = 0; i < s.length; i++){
    if(s[i] === s[i].toUpperCase() && isNaN(s[i])){
      sum += s[i].charCodeAt();
    }
  }
  return sum;
}
console.log(digitSum("abAB")); //131
console.log(digitSum("abcCd")); //67
console.log(digitSum("helloE")); //69
console.log(digitSum("woArBld")); //131
console.log(digitSum("aAaaaXa")); //153
console.log(digitSum("")); //0

//The function loops through every character in the string, checks if it is uppercase using the isNaN function and if it is uppercase, it adds its ASCII value to the sum. The function then returns the sum.
//The function is case sensitive and does not consider numbers.
//The ASCII value of 'A' is 65 and of 'E' is 69, so the sum of their ASCII values for the string "helloE" is 69.
//The ASCII value of 'A' is 65, 'a' is 97 and 'X' is 88, so the sum of their ASCII values for the string "aAaaaXa" is 153.
//If the string is empty, the function returns 0 as there are no uppercase letters to add to the sum.

//The time complexity of this function is O(n), where n is the length of the string, because it needs to traverse the string once to calculate the sum of the ASCII values.
//The space complexity is O(1), because it uses a constant amount of space to store the sum and the string character.
















































































