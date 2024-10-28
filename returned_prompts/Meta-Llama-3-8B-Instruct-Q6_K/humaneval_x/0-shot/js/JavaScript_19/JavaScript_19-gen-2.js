```
const sortNumbers = (numbers) => {
  const numMap = {
    zero: 0, one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9
  };
  const numbersArray = numbers.split(' ');
  const sortedNumbers = numbersArray.sort((a, b) => numMap[a] - numMap[b]);
  return sortedNumbers.join(' ');
};
```



Explanation:
1. We create an object `numMap` that maps the string representation of numbers to their integer values.
2. We split the input string into an array of numbers using the `split` method with a space character as the separator.
3. We use the `sort` method to sort the array of numbers. The `sort` method takes a compare function as an argument. In this case, we use an arrow function that returns the difference between the integer values of two numbers. This will sort the numbers in ascending order.
4. Finally, we join the sorted array of numbers back into a string using the `join` method with a space character as the separator.
5. The resulting string is the sorted string of numbers.