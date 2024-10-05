To solve this problem we need to create a function that takes in an array and returns an array with all the unique elements sorted. We can do this by using the Set object in JavaScript, which allows us to store unique values. Here's a step-by-step guide on how to solve this problem:

1. Define the function `unique` that takes in an array `l` as a parameter.
2. Convert the array `l` into a Set using the spread operator `...`. This will remove all duplicate elements from the array.
3. Convert the Set back into an array using the spread operator `...` again. This will give us an array with all the unique elements.
4. Sort the array using the `sort` method and a comparison function that compares the elements in ascending order. In this case, we can use the `(a, b) => a - b` function to ensure the elements are sorted numerically.
5. Return the sorted array.

Here's the final code for the `unique` function:

```javascript
const unique = (l) => {
  const set = new Set(l);
  const sorted = [...set].sort((a, b) => a - b);
  return sorted;
};
```

You can test the function with the example provided:

```javascript
console.log(unique([5, 3, 5, 2, 3, 3, 9, 0, 123])); // [0, 2, 3, 5, 9, 123]
```

This will output `[0, 2, 3, 5, 9, 123]`, which are all the unique elements in the array sorted in ascending order.

In addition to this solution, it's worth noting that using a Set object is not the only way to solve this problem. You can also use other methods like `filter` and `sort` to achieve the same result. However, using a Set is generally more efficient and concise, especially for larger arrays.

I hope this helps you understand how to solve this problem using JavaScript! Let me know if you have any more questions.
```

...

Answer: To solve this problem, you can define a function called `unique` that