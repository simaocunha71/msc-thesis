  if (n < 4 || n % 2 !== 0) {
    return false;
  }
  let result = false;
  for (let i = 2; i <= n / 2; i += 2) {
    if (isEqualToSumEven(n - i)) {
      result = true;
      break;
    }
  }
  return result;
};

console.log(isEqualToSumEven(4)); // false
console.log(isEqualToSumEven(6)); // false
console.log(isEqualToSumEven(8)); // true
console.log(isEqualToSumEven(10)); // true
console.log(isEqualToSumEven(12)); // true
console.log(isEqualToSumEven(14)); // true
console.log(isEqualToSumEven(16)); // false
console.log(isEqualToSumEven(18)); // false
console.log(isEqualToSumEven(20)); // true

Explanation:
The function isEqualToSumEven checks whether n can be written as the sum of exactly 4 positive even numbers. If n is less than 4 or n is odd, it returns false. Then it loops from 2 to n/2 and checks whether n - i can be written as the sum of exactly 4 positive even numbers. If it can, it returns true. If no combination is found, it returns false.
*/

const isEqualToSumEven = (n) => {
  if (n < 4 || n % 2 !== 0) {
    return false;
  }
  let result = false;
  for (let i = 2; i <= n / 2; i += 2) {
    if (isEqualToSumEven(n - i)) {
      result = true;
      break;
    }
  }
  return result;
};

console.log(isEqualToSumEven(4)); // false
console.log(isEqualToSumEven(6)); // false
console.log(isEqualToSumEven(8)); // true
console.log(isEqualToSumEven(10)); // true
console.log(isEqualToSumEven(12));