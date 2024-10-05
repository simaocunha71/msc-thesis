Here is a possible implementation of the `totalMatch` function in JavaScript:
```
const totalMatch = (lst1, lst2) => {
  const totalChars1 = lst1.reduce((acc, str) => acc + str.length, 0);
  const totalChars2 = lst2.reduce((acc, str) => acc + str.length, 0);
  if (totalChars1 < totalChars2) return lst1;
  if (totalChars1 > totalChars2) return lst2;
  return lst1;
};
```
Here's an explanation of how the function works:

1. We use the `reduce` method to calculate the total number of characters in each list. The `reduce` method takes a callback function as an argument, which is called for each element in the list, and returns the accumulated result.
2. We compare the total number of characters in each list. If `lst1` has fewer characters, we return `lst1`. If `lst2` has fewer characters, we return `lst2`.
3. If the two lists have the same number of characters, we return the first list (`lst1`) because the problem statement specifies that if the lists have the same number of chars, return the first list.

You can test the function with the examples provided in the problem statement to see that it returns the expected results.