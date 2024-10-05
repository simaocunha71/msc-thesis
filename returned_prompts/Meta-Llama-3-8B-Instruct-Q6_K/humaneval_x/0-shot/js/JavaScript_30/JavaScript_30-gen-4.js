```javascript
const getPositive = (l) => l.filter(n => n > 0);
```


Explanation:
The task is to create a function `getPositive` that takes a list of numbers as input and returns a new list containing only the positive numbers from the original list.

The function uses the `filter` method, which is a part of the JavaScript array prototype, to create a new array with only the elements that pass the test implemented by the provided function.

In this case, the function `n => n > 0` is a lambda function that takes each element `n` in the array and checks if it's greater than 0. If it is, the element is included in the new array.

Here's an example usage of the function:
```javascript
const numbers = [-1, 2, -4, 5, 6];
const positiveNumbers = getPositive(numbers);
console.log(positiveNumbers); // Output: [2, 5, 6]
```
This code would output `[2, 5, 6]`, which are the positive numbers from the original list.