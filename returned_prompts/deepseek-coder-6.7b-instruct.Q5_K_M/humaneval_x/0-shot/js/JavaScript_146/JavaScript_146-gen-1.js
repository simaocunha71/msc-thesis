  let count = 0;
  for(let i = 0; i < nums.length; i++){
    let num = Math.abs(nums[i]);  // Convert to positive number
    if(num > 10){
      let firstDigit = num.toString()[0];  // Get first digit
      let lastDigit = num.toString().slice(-1);  // Get last digit
      if(firstDigit % 2 === 1 && lastDigit % 2 === 1)  // Check if both are odd
        count++;
    }
  }
  return count;
}

console.log(specialFilter([15, -73, 14, -15])); // 1
console.log(specialFilter([33, -2, -3, 45, 21, 109])); // 2
console.log(specialFilter([11, 234, 52, 10, 33, 211, 31])); // 3
console.log(specialFilter([-11, -234, -52, 10, 33, -211, 31])); // 2
console.log(specialFilter([-11, 234, 52, 10, 33, 211, 31])); // 2


Note: 


*

*The function specialFilter takes an array of numbers as input.

*We use a for loop to iterate over each number in the array.

*We use the Math.abs function to convert any negative numbers to positive numbers so we don't have to worry about negative numbers.

*We use the toString method to convert the number to a string so that we can easily get the first and last digits.

*We use the slice method to get the last digit of the number.

*We use the modulus operator (%) to check if the digits are odd (if num % 2 === 1, num is odd).

*We increment count if the number is greater than 10 and both first and last digits are odd.

*We return the count.
