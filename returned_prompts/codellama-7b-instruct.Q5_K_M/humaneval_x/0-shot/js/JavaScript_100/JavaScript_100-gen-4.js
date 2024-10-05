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
    const pile = [n];
    for (let i = 1; i < n; i++) {
      if (n % 2 === 0) {
        pile.push(n + 2 * i);
      } else {
        pile.push(n + 2 * i + 1);
      }
    }
    return pile;
  };

