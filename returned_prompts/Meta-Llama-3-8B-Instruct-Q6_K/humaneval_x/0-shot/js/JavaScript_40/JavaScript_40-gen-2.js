```
  const seen = new Set();
  for (let num of l) {
    const complement = -num;
    if (seen.has(complement)) {
      return true;
    }
    for (let num2 of l) {
      if (num === num2) continue;
      const sum = num + num2;
      if (seen.has(sum)) {
        return true;
      }
      seen.add(num2);
    }
  }
  return false;
```
This function iterates over the list of numbers, for each number, it checks if its negative is in the set of seen numbers, if it is, it returns true. If not, it iterates over the list again, for each number, it checks if the sum of the current number and the previous number is in the set of seen numbers, if it is, it returns true. If not, it adds the current number to the set of seen numbers. If it goes through the whole list without finding a triplet that sums to zero, it returns false. This way, it has a time complexity of O(n^2) where n is the length of the list.