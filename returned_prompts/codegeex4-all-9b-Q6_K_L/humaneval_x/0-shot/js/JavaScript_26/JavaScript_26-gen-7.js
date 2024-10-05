You can solve this problem by using a Set to track the unique numbers and a for loop to iterate through the array. Here's how you can implement this:

```javascript
const removeDuplicates = (numbers) => {
  const uniqueNumbers = new Set();
  const result = [];
  
  for (let i = 0; i < numbers.length; i++) {
    if (!uniqueNumbers.has(numbers[i])) {
      uniqueNumbers.add(numbers[i]);
      result.push(numbers[i]);
    }
  }
  
  return result;
};
```

This function will iterate through the input array and add each unique number to the Set. It will also add the unique number to the result array. Finally, it will return the result array.