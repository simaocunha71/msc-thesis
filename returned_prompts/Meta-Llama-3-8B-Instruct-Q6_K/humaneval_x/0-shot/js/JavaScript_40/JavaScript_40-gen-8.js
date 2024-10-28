```
function triplesSumToZero(l) {
  l = l.sort((a, b) => a - b);
  for (let i = 0; i < l.length - 2; i++) {
    let left = i + 1;
    let right = l.length - 1;
    while (left < right) {
      let sum = l[i] + l[left] + l[right];
      if (sum === 0) {
        return true;
      } else if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
  }
  return false;
}
```


The time complexity of this solution is O(n^2), where n is the length of the input list. The space complexity is O(n), as we are sorting the list.

This function sorts the input list in ascending order, then it uses two pointers, one at the left and one at the right of the list, to find a triplet that sums to zero. If the sum is less than zero, we move the left pointer to the right, and if the sum is greater than zero, we move the right pointer to the left. If we find a triplet that sums to zero, we return true. If we finish the loop without finding such a triplet, we return false.