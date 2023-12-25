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
  let numOfStones = [];
  if (!n || typeof n !== 'number') return null;
  let i = 1, j = 0;
  while (i <= n && !isNaN(j)) {
    if (i % 2 === 0) j += parseInt(5 * (i - parseInt(i / 2)));
    else j += parseInt(7 * i);
    numOfStones.push(j);
    i++;
  }
  return numOfStones;
}
module.exports = makeAPile;