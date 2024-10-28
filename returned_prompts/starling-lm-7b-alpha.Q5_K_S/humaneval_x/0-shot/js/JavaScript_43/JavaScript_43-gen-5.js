To solve this problem, I would use a set to keep track of the numbers I have already seen. Then, for each number in the array, I would check if the negative of that number is in the set. If it is, then we have found two distinct elements that sum to zero, and we can return true. Otherwise, I would add the number to the set and continue with the next number. If I iterate through the entire array and never find two elements that sum to zero, then I can return false.

Here's the implementation of the function in JavaScript:

```javascript
const pairsSumToZero = (l) => {
  const seen = new Set();
  for (let i = 0; i < l.length; i++) {
    if (seen.has(-l[i])) {
      return true;
    } else {
      seen.add(l[i]);
    }
  }
  return false;
};
```

This implementation has a time complexity of O(n), where n is the length of the input list, because we iterate through the list once. The space complexity is O(n) as well, because the set can have up to n elements in the worst case, when all the elements in the list are distinct.

It's important to note that this implementation assumes that the input list does not contain any negative zeros. If the list can contain negative zeros, we would need to modify the implementation slightly to handle them correctly.

Here's the modified implementation that can handle negative zeros:

```javascript
const pairsSumToZero = (l) => {
  const seen = new Set();
  for (let i = 0; i < l.length; i++) {
    if (seen.has(-l[i])) {
      return true;
    } else if (l[i] === 0) {
      if (seen.has(0)) {
        return true;
      } else {
        seen.add(0);
      }
    } else {
      seen.add(l[i]);
    }
  }
  return false;
};
```

This modified implementation still has a time complexity of O(n) and a space complexity of O(n).

In summary, the pairs