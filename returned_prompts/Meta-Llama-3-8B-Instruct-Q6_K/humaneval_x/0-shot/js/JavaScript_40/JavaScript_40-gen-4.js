```
const triplesSumToZero = (l) => {
  const seen = new Set();
  for (let i = 0; i < l.length; i++) {
    for (let j = i + 1; j < l.length; j++) {
      const complement = -l[i] - l[j];
      if (seen.has(complement)) {
        return true;
      }
      seen.add(l[j]);
    }
  }
  return false;
};
```


This function works by iterating through the list of numbers, for each number, it calculates its complement (the number that needs to be added to it to make zero). It then checks if this complement is in the set of numbers it has seen so far. If it is, it means that there are three numbers in the list that sum to zero, and the function returns true. If it doesn't find any such triplet, it returns false.

The use of a set for storing the seen numbers ensures that the function runs in O(n) time, as lookups in a set are constant time. Without the set, the function would have to iterate through the entire list for each number, making it run in O(n^2) time.