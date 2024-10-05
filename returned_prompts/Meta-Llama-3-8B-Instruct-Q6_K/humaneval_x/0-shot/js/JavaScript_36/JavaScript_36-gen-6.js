```
const fizzBuzz = (n) => {
  let count = 0;
  for (let i = 1; i < n; i++) {
    if (i % 11 === 0 || i % 13 === 0) {
      count += (i + '').split('').filter(c => c === '7').length;
    }
  }
  return count;
};
```


This function works by iterating over all numbers less than `n` and checking if they are divisible by 11 or 13. If they are, it counts the number of times the digit 7 appears in the number by converting it to a string, splitting it into individual characters, filtering those characters to only include '7', and then getting the length of the resulting array. This count is added to the total count and the function returns the total count. 





This solution uses a for loop to iterate over all numbers less than `n`. It uses the modulus operator (`%`) to check if each number is divisible by 11 or 13. If the number is divisible by either of these numbers, it converts the number to a string, splits the string into individual characters, filters those characters to only include '7', and then gets the length of the resulting array. This count is added to the total count. The function returns the total count.