```
function pairsSumToZero(l) {
  const seen = new Set();
  for (const num of l) {
    const complement = -num;
    if (seen.has(complement)) {
      return true;
    }
    seen.add(num);
  }
  return false;
}
```


Explanation:
The function `pairsSumToZero` takes a list of integers `l` as input and returns `true` if there are two distinct elements in the list that sum to zero, and `false` otherwise.

The function uses a `Set` called `seen` to keep track of the elements it has seen so far. It iterates over the list, and for each element `num`, it calculates its complement `-num`. If the complement is already in the `seen` set, it means that there are two distinct elements in the list that sum to zero, and the function returns `true`. Otherwise, it adds the current element to the `seen` set.

The function returns `false` if it iterates over the entire list without finding a pair of elements that sum to zero.

The time complexity of this function is O(n), where n is the length of the input list, because it iterates over the list once. The space complexity is also O(n), because in the worst case, it needs to store all elements in the `seen` set.