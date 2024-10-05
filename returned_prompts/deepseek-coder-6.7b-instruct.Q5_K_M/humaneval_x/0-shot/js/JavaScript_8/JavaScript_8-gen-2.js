  let sum = 0;
  let product = 1;

  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
    product *= numbers[i];
  }

  return (sum, product);
}
console.log(sumProduct([1, 2, 3, 4]));

// or

const sumProduct = (numbers) => {
  let sum = 0;
  let product = 1;

  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
    product *= numbers[i];
  }

  return (sum, product);
}
console.log(sumProduct([1, 2, 3, 4]));

// or

const sumProduct = (numbers) => {
  return numbers.reduce((acc, val) => (acc[0] += val, acc[1] *= val) ? acc : [0, 1], [0, 1]);
}
console.log(sumProduct([1, 2, 3, 4]));

// or

const sumProduct = (numbers) => {
  return numbers.reduce(([sum, product], n) => [sum + n, product * n], [0, 1]);
}
console.log(sumProduct([1, 2, 3, 4]));
```

In the final solution, a reduce method is used to accumulate a value by iterating over the elements of the array from left to right. In the process, a pair of sum and product of all the integers in the array is maintained. The reduce method takes a callback function which takes two arguments - an accumulator and a current value. The accumulator is an array where the first element is the sum and the second one is the product. In the callback function, the sum is increased by the current value and the product is multiplied by the current value. Finally, the accumulator is returned as the result.

Note that this solution uses ES6 arrow function syntax and the reduce method which are supported in modern JavaScript environments.

The final solution returns a tuple (in JavaScript, it's a special kind of array with a fixed