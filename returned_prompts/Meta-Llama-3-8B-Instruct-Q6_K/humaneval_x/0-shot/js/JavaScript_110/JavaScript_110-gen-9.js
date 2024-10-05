Here is a possible implementation of the function:

```javascript
const exchange = (lst1, lst2) => {
  let oddCount = 0;
  for (const num of lst1) {
    if (num % 2 !== 0) {
      oddCount++;
    }
  }
  for (const num of lst2) {
    if (num % 2 !== 0) {
      oddCount--;
    }
  }
  return oddCount === 0 ? "YES" : "NO";
};
```

This function works by first counting the number of odd numbers in lst1. Then, it counts the number of odd numbers in lst2. If the difference between these two counts is 0, it means that it is possible to exchange elements between lst1 and lst2 to make all the elements of lst1 even. In this case, the function returns "YES". Otherwise, it returns "NO". 

For example, if we call `exchange([1, 2, 3, 4], [1, 2, 3, 4])`, the function will return "YES" because we can exchange elements between the two lists to make all the elements of lst1 even. On the other hand, if we call `exchange([1, 2, 3, 4], [1, 5, 3, 4])`, the function will return "NO" because there is no way to exchange elements between the two lists to make all the elements of lst1 even. 

This function assumes that the input lists will be non-empty, as specified in the problem statement. If the input lists can be empty, we would need to add additional error checking code to handle this case. 