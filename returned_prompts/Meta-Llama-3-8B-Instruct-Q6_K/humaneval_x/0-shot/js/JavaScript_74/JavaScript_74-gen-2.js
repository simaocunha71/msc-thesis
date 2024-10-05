Here is a JavaScript function that solves the problem:

```javascript
const totalMatch = (lst1, lst2) => {
  const sum1 = lst1.reduce((acc, current) => acc + current.length, 0);
  const sum2 = lst2.reduce((acc, current) => acc + current.length, 0);
  
  if (sum1 < sum2) {
    return lst1;
  } else if (sum1 > sum2) {
    return lst2;
  } else {
    return lst1;
  }
};
```

This function uses the `reduce()` method to calculate the total number of characters in each list. It then compares these sums and returns the list with the smaller sum. If the sums are equal, it returns the first list. 

Note that this function is case sensitive, so 'hi' and 'Hi' are considered different strings. If you want a case-insensitive comparison, you can convert the strings to lowercase or uppercase before comparing them. 

Also, this function does not handle the case where the input lists contain non-string elements. You may want to add error checking to handle this possibility. 