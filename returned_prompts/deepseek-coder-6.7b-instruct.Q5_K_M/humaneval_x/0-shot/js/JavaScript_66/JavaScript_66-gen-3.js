  let sum = 0;
  for(let i = 0; i < s.length; i++){
    let code = s.charCodeAt(i);
    if(code >= 65 && code <= 90){
      sum += code;
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

//In this function, we first initialize a variable sum to keep track of the total sum.
//Next, we iterate over the string s using a for loop. 
//For each character in the string, we get its ASCII value by using the charCodeAt method.
//We then check if the ASCII value falls within the range of uppercase letters (65-90). 
//If it does, we add it to the sum. 
//Finally, we return the sum.
//The ASCII value for 'A' is 65 and for 'Z' is 90.
//In JavaScript, the charCodeAt method returns a UTF-16 code unit integer representing the UTF-16 code unit at the given index.
//The sum of the ASCII values of the uppercase letters in the alphabet is the sum of the ASCII values of all uppercase letters.
//So, we can use this property to solve the problem.
//The time complexity of this function is O(n), where n is the length of the string.
//The space complexity is O(1), as we only use a constant amount of space to store the sum and the ASCII values.
//This function works for any string input as it only considers uppercase letters and ignores the rest.
//It's also case-sensitive, meaning it treats lowercase and uppercase letters as different characters.
//It should work for any string of any length and any characters.
//If the string is empty, the function will return