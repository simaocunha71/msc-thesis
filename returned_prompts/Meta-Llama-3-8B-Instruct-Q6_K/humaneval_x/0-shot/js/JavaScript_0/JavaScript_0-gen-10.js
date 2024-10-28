Here is the solution to the problem:
```
const hasCloseElements = (numbers, threshold) => {
  numbers.forEach((num, i) => {
    for (let j = i + 1; j < numbers.length; j++) {
      if (Math.abs(num - numbers[j]) < threshold) {
        return true;
      }
    }
  });
  return false;
};
```
This function iterates over the list of numbers and checks if any two numbers are closer to each other than the given threshold. If it finds such a pair, it returns `true`. If it doesn't find any such pair after checking all numbers, it returns `false`.

Here is the breakdown of the solution:

* We use a nested loop to iterate over the list of numbers. The outer loop iterates over each number in the list, and the inner loop iterates over the remaining numbers in the list (starting from the next number after the current number).
* For each pair of numbers, we calculate the absolute difference between the two numbers using `Math.abs(num - numbers[j])`.
* If the absolute difference is less than the threshold, we return `true` immediately, because we have found a pair of numbers that are closer to each other than the threshold.
* If we reach the end of the function without finding a pair of numbers that are closer to each other than the threshold, we return `false`.

You can test the function with the examples you provided:
```
console.log(hasCloseElements([1.0, 2.0, 3.0], 0.5)); // false
console.log(hasCloseElements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)); // true
````
I hope this helps! Let me know if you have any questions.