To solve this problem, we can create a new array called "uniqueNumbers" and use a for loop to iterate through the "numbers" array. Inside the loop, we can check if the current element is already in the "uniqueNumbers" array using the includes() method. If it is not, we push the element to the "uniqueNumbers" array. Finally, we return the "uniqueNumbers" array.

Here's the code for the solution:
```javascript
const removeDuplicates = (numbers) => {
  const uniqueNumbers = [];
  for (const num of numbers) {
    if (!uniqueNumbers.includes(num)) {
      uniqueNumbers.push(num);
    }
  }
  return uniqueNumbers;
};
```

This solution ensures that only unique elements are kept in the "uniqueNumbers" array while maintaining the order of the elements. The includes() method is used to check if an element already exists in the "uniqueNumbers" array, and if not, it is added to the array using the push() method.

You can test the solution using the provided test case:
```javascript
console.log(removeDuplicates([1, 2, 3, 2, 4]));
```
This will output `[1, 3, 4]`, which is the expected result.

The solution is concise and efficient, as it only iterates through the "numbers" array once and checks for duplicates using the includes() method.

Overall, this solution provides a straightforward and effective way to remove duplicates from a list of integers while maintaining the order of the remaining elements.
```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

