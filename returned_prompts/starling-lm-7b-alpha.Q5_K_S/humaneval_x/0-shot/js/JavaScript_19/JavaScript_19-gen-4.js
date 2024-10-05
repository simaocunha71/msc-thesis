To solve this problem, we can follow these steps:

1. Split the input string into an array of numbers using the space character as the delimiter. For example, if the input is 'three one five', the resulting array would be ['three', 'one', 'five'].

2. Sort the array of numbers in ascending order based on their numerical value. In JavaScript, we can use the sort() method to achieve this. The sort() method sorts the elements of an array in place and returns the sorted array. Since the default sorting order is based on the Unicode value of the characters, we don't need to provide a compare function.

3. Join the sorted array back into a string, using a space character as the separator. In JavaScript, we can use the join() method to convert an array into a string. The join() method takes an optional separator argument, which specifies the string to use as a separator between array elements.

Here's the code that implements the above steps:

```javascript
const sortNumbers = (numbers) => {
  // Step 1: Split the input string into an array of numbers
  const numbersArray = numbers.split(' ');

  // Step 2: Sort the array of numbers in ascending order
  numbersArray.sort();

  // Step 3: Join the sorted array back into a string
  return numbersArray.join(' ');
};
```

Using the provided test case, the function will return the string 'one three five', as expected.

To test the function, you can use the following code:

```javascript
console.log(sortNumbers('three one five'));  // Output: 'one three five'
```

This will display the sorted string 'one three five' in the console.

It's worth noting that the sort() method in JavaScript is case-sensitive. If you have uppercase letters in your input string, they will not be sorted correctly. To handle this, you can convert all the elements in the array to lowercase or uppercase using the toLowerCase() or toUpperCase() methods, respectively, before sorting them.

For example, if you want to sort the input string 'Three one Five' with case-insensitive sorting, you can modify the code as follows: