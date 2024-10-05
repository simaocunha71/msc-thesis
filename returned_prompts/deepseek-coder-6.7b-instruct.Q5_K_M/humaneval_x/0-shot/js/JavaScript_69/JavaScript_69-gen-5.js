  const frequency = lst.reduce((acc, curr) => {
    acc[curr] = (acc[curr] || 0) + 1;
    return acc;
  }, {});

  let max = -1;

  for (let num in frequency) {
    if (frequency[num] >= num) {
      max = Math.max(max, num);
    }
  }

  return max;
};

console.log(search([4, 1, 2, 2, 3, 1])); // 2
console.log(search([1, 2, 2, 3, 3, 3, 4, 4, 4])); // 3
console.log(search([5, 5, 4, 4, 4])); // -1

```

This program works by first creating a frequency object that maps each number in the list to its frequency. Then it iterates over the numbers in the frequency object, and if the frequency of a number is greater than or equal to the number itself, it updates the max to be the maximum between the current max and the number. Finally, it returns the max.

The time complexity of this program is O(n) and the space complexity is O(n) where n is the length of the list.

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```
