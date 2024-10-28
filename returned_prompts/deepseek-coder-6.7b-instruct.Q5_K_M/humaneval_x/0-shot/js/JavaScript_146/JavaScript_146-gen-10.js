  let count = 0;
  
  for (let i = 0; i < nums.length; i++) {
    let num = Math.abs(nums[i]);
    if (num > 10 && num % 10 !== 0 && num % 10 % 2 !== 0) {
      let firstDigit = parseInt(num.toString().charAt(0));
      if (firstDigit % 2 !== 0) {
        count++;
      }
    }
  }
  return count;
}

console.log(specialFilter([15, -73, 14, -15])); // 1
console.log(specialFilter([33, -2, -3, 45, 21, 109])); // 2

Explanation:
1. Define a variable count to keep track of the numbers that meet the criteria.
2. Iterate through the array of numbers.
3. For each number in the array, check if it is greater than 10 and if its last digit is odd (num % 10 % 2 !== 0).
4. If the number meets the first condition, check if the first digit of the number is also odd (parseInt(num.toString().charAt(0)) % 2 !== 0).
5. If the number meets all conditions, increment the count variable.
6. After checking all numbers in the array, return the count.
*/








































































































































































