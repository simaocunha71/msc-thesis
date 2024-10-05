  let negMax = null, posMin = null;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0 && (negMax === null || lst[i] > negMax)) negMax = lst[i];
    if (lst[i] > 0 && (posMin === null || lst[i] < posMin)) posMin = lst[i];
  }
  return [negMax, posMin];
}

console.log(largestSmallestIntegers([2, 4, 1, 3, 5, 7])); // [null, 1]
console.log(largestSmallestIntegers([])); // [null, null]
console.log(largestSmallestIntegers([0])); // [null, null]
```

This function loops through the list, checking each item if it is a negative number and if it is greater than the current maximum negative number, or if it is a positive number and if it is less than the current minimum positive number. If it is, it sets the appropriate variable to that number. It then returns the maximum negative and the minimum positive numbers as a list. If there are no negative or positive numbers, the variables will remain as null, and they will be returned.

The time complexity of this function is O(n), where n is the length of the list, as it loops through the list once. The space complexity is O(1), as it only uses a constant amount of space to store the maximum negative and minimum positive numbers.

This solution assumes that the input list will only contain integer numbers.
*/

const largestSmallestIntegers = (lst) => {
  let negMax = null, posMin = null;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0 && (negMax === null || lst[i] > negMax)) negMax = lst[i];
    if (lst[i] > 0 && (posMin === null || lst[i] < posMin)) posMin = lst[i];
  }
  return [negMax, posMin];
}

console.log(largest