Here is a solution for the problem:
```
const exchange = (lst1, lst2) => {
  // Filter out odd numbers from lst1
  const oddNumbersInLst1 = lst1.filter(num => num % 2 !== 0);

  // Check if all odd numbers in lst1 exist in lst2
  for (const num of oddNumbersInLst1) {
    if (!lst2.includes(num)) {
      return "NO";
    }
  }

  // If we have not returned "NO" yet, it means we can make lst1 a list of only even numbers
  return "YES";
};
```
Here's how it works:

1. We filter out the odd numbers from `lst1` and store them in `oddNumbersInLst1`.
2. We then check if all the odd numbers in `lst1` exist in `lst2`. If any odd number is not found in `lst2`, we return "NO".
3. If we have not returned "NO" yet, it means we can make `lst1` a list of only even numbers by exchanging elements with `lst2`. So, we return "YES".