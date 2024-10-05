  let sum = 0, product = 1;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
    product *= numbers[i];
  }
  return (sum, product);
}

// Test cases
console.log(sumProduct([])); // Expected output: (0, 1)
console.log(sumProduct([1, 2, 3, 4])); // Expected output: (10, 24)

// Explanation:
// In the first test case, we pass an empty array as argument, so sum and product both are 0 and 1 respectively.
// In the second test case, we pass an array [1, 2, 3, 4] as argument. Sum is 1 + 2 + 3 + 4 = 10 and product is 1 * 2 * 3 * 4 = 24. So, the expected output is (10, 24).

// Note: This function will work with any array of integers, not just the provided example.

// You can also use reduce method in JavaScript to achieve the same result. Here is the code:

const sumProduct 2= (numbers) => {
  const sum = numbers.reduce((total, num) => total + num, 0);
  const product = numbers.reduce((total, num) => total * num, 1);
  return (sum, product);
}

// This code will work in the same way as the previous one. It uses the reduce method to calculate the sum and the product of the numbers in the array.
```

## Instructions:

In the given problem, we are asked to return a tuple consisting of a sum and a product of all the integers in a list. If the list is empty, the sum should be 0 and the product should be 1.

Here, the function `sumProduct` is defined which takes a list of numbers as input and returns a tuple.

Inside the function, two variables `sum` and `product` are initialized to 0 and 1 respectively. Then a for loop is used to iterate over the elements of the input list. For each element, the value of the element is added to the `sum