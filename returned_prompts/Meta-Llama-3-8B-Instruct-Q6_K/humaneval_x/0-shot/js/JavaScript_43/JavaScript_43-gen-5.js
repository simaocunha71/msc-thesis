```
function pairsSumToZero(lst) {
  // Create a set to store the elements we've seen so far
  const seen = new Set();

  // Iterate over the list
  for (const num of lst) {
    // Calculate the complement of the current number
    const complement = -num;

    // Check if we've seen the complement before
    if (seen.has(complement)) {
      // If we have, return true
      return true;
    }

    // Add the current number to the set
    seen.add(num);
  }

  // If we've iterated over the entire list and haven't found a pair that sums to zero, return false
  return false;
}
```



Explanation:

This function uses a set to keep track of the numbers we've seen so far. We iterate over the list, and for each number, we calculate its complement (i.e., the number that would add up to zero if we subtracted it from the current number). We then check if the complement is in the set. If it is, we return true, because we've found a pair of numbers that sum to zero. If not, we add the current number to the set and continue iterating.

The time complexity of this function is O(n), where n is the length of the input list, because we're iterating over the list once. The space complexity is also O(n), because in the worst case, we're storing every element in the set. However, in practice, the space complexity is likely to be much smaller, because we're only storing distinct elements in the set.