  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    let num = Math.abs(nums[i]);
    if (num > 10 && (num % 10) % 2 === 1 && (num >= 10 && (num < 100 || (num >= 1000 && num < 10000) && (num % 100) % 2 === 1) || (num >= 100000 && (num % 1000) % 2 === 1))) {
      count++;
    }
  }
  return count;
}

console.log(specialFilter([15, -73, 14, -15]));
console.log(specialFilter([33, -2, -3, 45, 21, 109]));

// This function works by looping through each number in the input array. For each number, it checks if the number is greater than 10 and if the last digit and the first digit are odd. 
// If both conditions are met, it increments the count variable. Finally, it returns the count.
// The Math.abs function is used to ensure that negative numbers are treated as positive.
// The condition (num % 10) % 2 === 1 checks if the last digit of a number is odd.
// The condition (num >= 10 && (num < 100 || (num >= 1000 && num < 10000) && (num % 100) % 2 === 1) || (num >= 100000 && (num % 1000) % 2 === 1)) checks if the first and the last digits of a number are odd.
// This is done by checking if the last digit is odd (num % 10 % 2 === 1), and if the first and last digits are odd (num % 100 % 2 === 1, num % 1000 % 2 === 1, num % 10000 % 2 === 1, num % 100000 % 2 === 1).
// The condition num >= 100000 &&