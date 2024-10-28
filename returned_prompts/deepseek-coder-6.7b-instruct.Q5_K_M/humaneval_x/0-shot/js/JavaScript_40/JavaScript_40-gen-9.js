  l.sort((a, b) => a - b);

  for (let i = 0; i < l.length - 2; i++) {
    if (i > 0 && l[i] === l[i - 1]) continue;

    let j = i + 1;
    let k = l.length - 1;

    while (j < k) {
      const sum = l[i] + l[j] + l[k];

      if (sum < 0) {
        j++;
      } else if (sum > 0) {
        k--;
      } else {
        return true;
      }
    }
  }

  return false;
};

module.exports = triplesSumToZero;

```

## Solution

The solution uses the two-pointer technique, similar to two-sum problem. It first sorts the input list, then it loops through each element of the list, and for each element, it tries to find two other elements that sum to the negative of the current element. If it finds such two elements, it returns true; otherwise, it continues the loop. If it finishes the loop without finding such triplets, it returns false.

This solution has a time complexity of O(n^2), where n is the length of the list. This is because it has a nested loop structure, where for each element, it performs a binary search on the rest of the list. The space complexity is O(1), which means it uses a constant amount of extra memory.

## Test Cases

```javascript
console.log(triplesSumToZero([1, 3, 5, 0])); // false
console.log(triplesSumToZero([1, 3, -2, 1])); // true
console.log(triplesSumToZero([1, 2, 3, 7])); // false
console.log(triplesSumToZero([2, 4, -5, 3, 9, 7])); // true
console.log(triplesSumToZero([1])); // false
```

## Explanation

In the first test case, no three distinct numbers sum to zero.

In the second test case,