  let arr = [];

  for (let i = 0; i < n; i++) {
    if (n % 2 === 0) {
      arr.push(n + 2 * i);
    } else {
      arr.push(n + 2 * i);
    }
  }

  return arr;
}

console.log(makeAPile(3)); // [3, 5, 7]
console.log(makeAPile(4)); // [4, 6, 8, 10]
console.log(makeAPile(5)); // [5, 7, 9, 11, 13]
*/


const makeAPile = (n) => {
  let arr = [];

  for (let i = 0; i < n; i++) {
    if (n % 2 === 0) {
      arr.push(n + 2 * i);
    } else {
      arr.push(n + 2 * i);
    }
  }

  return arr;
}

console.log(makeAPile(3)); // [3, 5, 7]
console.log(makeAPile(4)); // [4, 6, 8, 10]
console.log(makeAPile(5)); // [5, 7, 9, 11, 13]


/*
  The function `makeAPile` takes a positive integer `n` as an argument, then it creates a new array `arr`.
  For each `i` from 0 to `n-1`, it pushes the number of stones in the level `i+1` to `arr`.
  If `n` is even, the number of stones in the level `i+1` is `n + 2*i`.
  If `n` is odd, the number of stones in the level `i+1` is `n + 2*i`.
  Finally, it returns the `arr`.

  This function works for any positive integer `n`.
  It generates the correct number of stones for each level of the pile, according to the problem statement.
*/







