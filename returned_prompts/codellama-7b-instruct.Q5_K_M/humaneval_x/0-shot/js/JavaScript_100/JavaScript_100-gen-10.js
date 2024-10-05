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
  const makeAPile = (n) => {
    let result = [];
    for (let i = 0; i < n; i++) {
      if (i % 2 === 0) {
        result.push(i + 1);
      } else {
        result.push(i + 2);
      }
    }
    return result;
  };
  return makeAPile(n);
};
