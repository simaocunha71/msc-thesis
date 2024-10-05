  let stones = [];
  let nextNumber = n;

  for (let i = 0; i < n; i++) {
    stones.push(nextNumber);
    nextNumber = nextNumber % 2 === 0 ? nextNumber + 2 : nextNumber + 1;
  }

  return stones;
}

console.log(makeAPile(3)); // [3, 5, 7]
*/

/*
