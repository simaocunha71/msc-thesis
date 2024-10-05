  let count = 0;

  for (let i = 0; i < n; i++) {
    if (i % 11 === 0 || i % 13 === 0) {
      count += (i.toString().match(/7/g) || []).length;
    }
  }

  return count;
};

console.log(fizzBuzz(50)); // 0
console.log(fizzBuzz(78)); // 2
console.log(fizzBuzz(79)); // 3

This is a JavaScript solution for the problem. It checks each number up to n to see if it is divisible by 11 or 13. If it is, it converts the number to a string and counts the number of times the character '7' appears. The total count is returned.
*/


// The above solution works but it can be optimized a bit. Instead of converting the number to a string and then counting the occurrences of '7', we can directly count the occurrences of '7' in the number itself.

const fizzBuzz = (n) => {
  let count = 0;

  for (let i = 0; i < n; i++) {
    if (i % 11 === 0 || i % 13 === 0) {
      let num = i;
      while (num > 0) {
        if (num % 10 === 7) {
          count++;
        }
        num = Math.floor(num / 10);
      }
    }
  }

  return count;
};

console.log(fizzBuzz(50)); // 0
console.log(fizzBuzz(78)); // 1
console.log(fizzBuzz(79)); // 2


/*
This optimized solution works by taking the number itself and checking each digit to see if it is '7'. If it is, we increment the count. We then repeat this process for the remaining digits of the number by performing an integer division by 10 on the number.
*/


/*
The time complexity of this solution is O(n), where n is the input number. This is because