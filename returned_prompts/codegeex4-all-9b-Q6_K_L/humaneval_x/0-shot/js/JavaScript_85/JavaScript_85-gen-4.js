You can solve this problem using JavaScript's array methods. Here's an example solution:

```javascript
const add = (lst) => {
  // Use the filter method to get all even numbers
  const evens = lst.filter((num) => num % 2 === 0);
  
  // Use the reduce method to add up all the even numbers
  const sum = evens.reduce((acc, num) => acc + num, 0);
  
  return sum;
};
```

This function first filters out all the even numbers from the input list using the `filter` method. Then, it adds up all the even numbers using the `reduce` method. Finally, it returns the sum.