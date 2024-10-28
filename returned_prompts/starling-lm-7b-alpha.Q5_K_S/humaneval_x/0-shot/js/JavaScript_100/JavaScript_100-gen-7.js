  let result = [];

  while (n > 0) {
    result.push(n);
    n = (n % 2 === 0) ? n + 1 : n + 2;
  }

  return result;
};

makeAPile(3) // [3, 5, 7]

*/

/*
  Given a positive integer n, you have to make a pile of n levels of stones.
  The first level has n stones.
  The number of stones in the next level is:
      - the next odd number if n is odd.
      - the next even number if n is even.
  Return the number of stones in each level in a list, where element at index
  i represents the number of stones in the level (i+1).

  Examples:
  >>> makeAPile(3)
  [3, 5, 7]
  */

makeAPile = (n) => {
  let result = [];

  while (n > 0) {
    result.push(n);
    n = (n % 2 === 0) ? n + 1 : n + 2;
  }

  return result;
};

makeAPile(3) // [3, 5, 7]

*/

// Time Complexity: O(n)
// Space Complexity: O(n)

// To handle large numbers, you can use BigInt instead of Number

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
