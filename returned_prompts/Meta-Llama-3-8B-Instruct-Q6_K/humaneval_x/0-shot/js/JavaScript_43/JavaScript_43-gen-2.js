```
  if (l.length < 2) return false;

  const seen = new Set();
  for (let num of l) {
    if (seen.has(-num)) return true;
    seen.add(num);
  }

  return false;
```
This function works by iterating over the list of numbers and keeping track of the numbers it has seen so far in a Set. If it sees a number that is the negative of a number it has seen before, it immediately returns true, because that means it has found two numbers that sum to zero. If it finishes iterating over the list without finding such a pair, it returns false.

The time complexity of this function is O(n), where n is the length of the input list, because it makes a single pass over the list. The space complexity is also O(n), because in the worst case it might have to store every number in the set. This is efficient for large inputs.