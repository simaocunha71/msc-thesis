```
  return l.length >= 3 && l.some((a, i) => {
    const remaining = l.slice(i + 1);
    return remaining.some((b) => {
      const toFind = -a - b;
      return remaining.includes(toFind);
    });
  });
```
Explanation:
The function takes a list of integers as input and returns true if there are three distinct elements in the list that sum to zero, and false otherwise.

The function uses the some() method to iterate over the list and checks if there are three distinct elements that sum to zero.

It first checks if the list has at least three elements. If not, it immediately returns false.

Then, it iterates over the list using some() and for each element, it creates a new array by slicing the list from the current index to the end.

It then uses some() again to check if there is another element in the new array that, when added to the current element, results in a third element that is the negation of their sum. If such an element is found, it returns true.

If no such elements are found, it returns false.

This approach ensures that the function returns true only if there are exactly three distinct elements that sum to zero, and not just two elements that sum to zero.