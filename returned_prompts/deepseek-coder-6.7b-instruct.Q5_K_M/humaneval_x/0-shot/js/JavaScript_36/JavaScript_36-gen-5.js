  let count = 0;

  for (let i=0; i<n; i++) {
    if (i % 11 === 0 || i % 13 === 0) {
      count += (i.toString().match(/7/g) || []).length;
    }
  }

  return count;
};

console.log(fizzBuzz(50));  // 0
console.log(fizzBuzz(78));  // 2
console.log(fizzBuzz(79));  // 3

```


## ✏️Explanation:

This problem involves creating a function that counts the number of times the digit 7 appears in numbers less than `n` which are divisible by 11 or 13.

First, the function initializes a counter variable `count` to 0. This counter will be used to keep track of the total number of times the digit 7 appears.

Then, a `for` loop is used to iterate through each number less than `n`. If the current number is divisible by 11 or 13 (i.e., `i % 11` or `i % 13` is equal to 0), the function converts the current number to a string and uses the `match` method with a regular expression to find all occurrences of the digit 7.

The `match` method returns an array of all matches, or `null` if no matches are found. Therefore, to avoid a TypeError when the `.length` property is accessed on `null`, the function uses an OR operator (`||`) to provide an empty array as a default value in the case that `match` returns `null`.

The length of the resultant array (which represents the number of times the digit 7 appears in the current number) is then added to the `count` variable.

Finally, the function returns the `count` variable, which represents the total number of times the digit 7 appears in numbers less than `n` which are divisible by 11 or 13.


## 🔑Key Points:

1. Use a `for` loop to iterate through each number less than `n