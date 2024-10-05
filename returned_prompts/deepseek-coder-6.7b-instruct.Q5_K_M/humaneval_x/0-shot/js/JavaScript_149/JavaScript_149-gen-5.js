  const oddLengthElements = lst.filter(element => element.length % 2 === 0);
  return oddLengthElements.sort((a, b) => a.length - b.length || a.localeCompare(b));
}

console.log(sortedListSum(["aa", "a", "aaa"]))
console.log(sortedListSum(["ab", "a", "aaa", "cd"]))

```

## 3. Create a function that takes an array of numbers as an argument and returns the sum of all the numbers.

