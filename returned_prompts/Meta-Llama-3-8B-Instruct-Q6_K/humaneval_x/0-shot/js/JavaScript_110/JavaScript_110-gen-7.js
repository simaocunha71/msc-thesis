Here is the solution:

```javascript
const exchange = (lst1, lst2) => {
  // Count the number of odd numbers in lst1
  let oddCount = 0;
  for (let num of lst1) {
    if (num % 2 !== 0) {
      oddCount++;
    }
  }

  // If the number of odd numbers in lst1 is greater than or equal to the length of lst2, it is impossible to make all elements of lst1 even
  if (oddCount >= lst2.length) {
    return "NO";
  }

  // Check if it is possible to make all elements of lst1 even by exchanging elements with lst2
  for (let num of lst1) {
    if (num % 2 !== 0) {
      // Find a matching odd number in lst2
      for (let num2 of lst2) {
        if (num2 % 2 !== 0) {
          // Exchange the numbers
          lst1[lst1.indexOf(num)] = num2;
          lst2[lst2.indexOf(num2)] = num;
          break;
        }
      }
    }
  }

  // If all elements of lst1 are even after exchanging, return "YES"
  for (let num of lst1) {
    if (num % 2 !== 0) {
      return "NO";
    }
  }
  return "YES";
};
```

The function first counts the number of odd numbers in lst1. If this count is greater than or equal to the length of lst2, it is impossible to make all elements of lst1 even, so the function returns "NO".

Then, the function checks if it is possible to make all elements of lst1 even by exchanging elements with lst2. It does this by iterating over the elements of lst1 and finding a matching odd number in lst2 for each odd number in lst1. If such a number is found, the function exchanges the numbers and breaks out of the inner loop. If no matching odd number is found, the function returns "NO".

Finally, the function checks if all elements of lst1 are even after exchanging. If they are, the function returns "YES". Otherwise, it returns "NO".