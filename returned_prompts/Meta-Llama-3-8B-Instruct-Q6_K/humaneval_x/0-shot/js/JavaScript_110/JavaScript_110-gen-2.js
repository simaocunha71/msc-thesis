Here is a possible solution for the problem:

```javascript
const exchange = (lst1, lst2) => {
  let oddCount = 0;
  for (let num of lst1) {
    if (num % 2 !== 0) {
      oddCount++;
    }
  }
  for (let num of lst2) {
    if (num % 2 !== 0) {
      oddCount--;
      if (oddCount < 0) {
        return "NO";
      }
    }
  }
  return "YES";
};
```

This function works by first counting the number of odd numbers in lst1. Then, it goes through each number in lst2 and decrements the odd count if the number is odd. If the odd count becomes negative, it means that there are more odd numbers in lst2 than in lst1, so it is not possible to make all the numbers in lst1 even by exchanging elements with lst2. If the function finishes going through all the numbers in lst2 without the odd count becoming negative, it returns "YES", because it is possible to make all the numbers in lst1 even by exchanging elements with lst2.