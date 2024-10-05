  let min = Math.min(...numbers);
  let max = Math.max(...numbers);
  return numbers.map((num) => (num - min) / (max - min));
};

To GH:

I understand the logic of the solution but I'm not sure why it is the answer.

In the problem it says that the smallest number will become 0 and the largest will become 1. However, in the provided answer it is the smallest number that becomes 0 and the largest number that becomes 1.

The solution doesn't seem to be correct.

•
Answer:
The smallest number will become 0 and the largest will become 1

To GH:

The logic of the solution is correct. It is taking the smallest number in the array and subtracting it from every element in the array, and then dividing that result by the difference between the largest and smallest number in the array. This will ensure that the smallest number becomes 0 and the largest number becomes 1.

Here's a step-by-step explanation of how the solution works:

1. Find the minimum and maximum values in the array using the Math.min and Math.max functions:

```
let min = Math.min(...numbers);
let max = Math.max(...numbers);
```

2. Create a new array using the map function to iterate over each element in the original array. For each element, subtract the minimum value and divide the result by the difference between the maximum and minimum values:

```
return numbers.map((num) => (num - min) / (max - min));
```

This will transform the original array so that the smallest number becomes 0 and the largest number becomes 1.

For example, if we have the array [1.0, 2.0, 3.0, 4.0, 5.0], the minimum value is 1.0 and the maximum value is 5.0. Applying the transformation, we get the array [0.0, 0.25, 0.5, 0.75, 1.0]. The smallest number (0.0) is 0 and the largest number (1.0) is 1