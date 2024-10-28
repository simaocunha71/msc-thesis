  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 10 && isOdd(nums[i])) {
      count++;
    }
  }
  return count;
}

const isOdd = (num) => {
  let firstDigit = Math.abs(num)
  while (firstDigit >= 10) {
    firstDigit = Math.floor(firstDigit / 10);
  }
  const lastDigit = Math.abs(num % 10);
  
  return firstDigit % 2 !== 0 && lastDigit % 2 !== 0;
}

console.log(specialFilter([15, -73, 14, -15]));
console.log(specialFilter([33, -2, -3, 45, 21, 109]));

/*
The function isOdd checks whether the first and last digits of a number are odd by first isolating the first digit, then checking if it's odd and finally checking the last digit.
The function specialFilter iterates over the array and increases the count if the number is greater than 10 and both first and last digits are odd.
*/
```

## Solution:

```javascript
const specialFilter = (nums) => {
  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 10 && isOdd(nums[i])) {
      count++;
    }
  }
  return count;
}

const isOdd = (num) => {
  let firstDigit = Math.abs(num)
  while (firstDigit >= 10) {
    firstDigit = Math.floor(firstDigit / 10);
  }
  const lastDigit = Math.abs(num % 10);
  
  return firstDigit % 2 !== 0 && lastDigit % 2 !== 0;
}

console.log(specialFilter([15