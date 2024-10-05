```
const orderByPoints = (nums) => {
  if (!nums.length) return [];
  return nums.sort((a, b) => {
    const sumA = a.toString().split('').reduce((acc, curr) => acc + parseInt(curr), 0);
    const sumB = b.toString().split('').reduce((acc, curr) => acc + parseInt(curr), 0);
    if (sumA === sumB) {
      return nums.indexOf(a) - nums.indexOf(b);
    }
    return sumA - sumB;
  });
};
```


Explanation:

1. We start by checking if the input list `nums` is empty. If it is, we return an empty list.
2. We define the `orderByPoints` function that takes a list of integers as input.
3. We use the `sort` method to sort the list in-place.
4. Inside the sorting callback function, we calculate the sum of the digits for each number `a` and `b` using the `toString`, `split`, `reduce`, and `parseInt` methods.
5. If the sums are equal, we use the original index of the numbers to break the tie. We do this by using the `indexOf` method to get the index of each number in the original list and then subtracting the indices.
6. If the sums are not equal, we simply return the difference between the sums.
7. Finally, the sorted list is returned.