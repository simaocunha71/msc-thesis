```
const triplesSumToZero = (l) => {
  if (l.length < 3) return false;
  l.sort((a, b) => a - b);
  for (let i = 0; i < l.length - 2; i++) {
    let left = i + 1;
    let right = l.length - 1;
    while (left < right) {
      let sum = l[i] + l[left] + l[right];
      if (sum === 0) return true;
      if (sum < 0) left++;
      else right--;
    }
  }
  return false;
};
```



Explanation:
1.  We first check if the list has less than 3 elements. If it does, we immediately return `false` because it's impossible to find three distinct elements that sum to zero.
2.  We sort the list in ascending order. This is because we're going to use two pointers, one starting from the next element and one from the end of the list, and we want to find the closest pair of elements that sum to the negation of the current element.
3.  We use a two-pointer technique. We initialize two pointers, `left` and `right`, to the next element and the last element of the list, respectively. We then enter a while loop that continues as long as `left` is less than `right`.
4.  Inside the loop, we calculate the sum of the current element, the element at `left`, and the element at `right`. If the sum is zero, we return `true` because we've found three distinct elements that sum to zero.
5.  If the sum is less than zero, we increment `left` to make the sum larger. If the sum is greater than zero, we decrement `right` to make the sum smaller.
6.  If the loop finishes without finding a sum of zero, we return `false` because it's impossible to find three distinct elements that sum to zero in the list.

This solution has a time complexity of O(n log n) due to the sorting, where n is the length of the list. The two-pointer technique inside the loop has a time complexity of O(n), but since it's nested inside the sorting, the overall time complexity is O(n log n). The space complexity is O(1) because we only use a constant amount of space to store the pointers and the sum.