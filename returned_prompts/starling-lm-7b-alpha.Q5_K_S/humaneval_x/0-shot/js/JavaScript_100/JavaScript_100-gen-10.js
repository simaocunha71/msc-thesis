  let stones = [];

  while (n > 0) {
    stones.push(n);
    n = (n % 2 === 0) ? n + 1 : n + 2;
  }

  return stones;
};

makeAPile(3); // [3, 5, 7]

*/

makeAPile(3); // [3, 5, 7]

// Solution 2
/*
const makeAPile = n => {
  let pile = [];

  while (n > 0) {
    pile.push(n);
    n = (n % 2 === 0) ? (n + 1) : (n + 2);
  }

  return pile;
};

makeAPile(3); // [3, 5, 7]
*/

// Solution 3
/*
const makeAPile = n => {
  let pile = [];

  while (n > 0) {
    pile.push(n);
    n = n % 2 === 0 ? n + 1 : n + 2;
  }

  return pile;
};

makeAPile(3); // [3, 5, 7]
*/


























































































































































































































