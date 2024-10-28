  let arr = [];
  let stones = n;

  for (let i = 0; i < n; i++) {
    arr.push(stones);
    if (stones % 2 === 0) {
      stones += 2;
    } else {
      stones += 2;
    }
  }

  return arr;
}

console.log(makeAPile(3)); // [3, 5, 7]

*/

function makeAPile(n) {
  let arr = [];
  let stones = n;

  for (let i = 0; i < n; i++) {
    arr.push(stones);
    if (stones % 2 === 0) {
      stones += 2;
    } else {
      stones += 2;
    }
  }

  return arr;
}

console.log(makeAPile(3)); // [3, 5, 7]

/* 
  Explanation:
  The makeAPile function takes in a number n and creates an empty array arr.
  Then, a variable stones is initialized to n. 
  The for loop iterates n times and pushes the current value of stones into the array arr.
  If stones is even, then stones is incremented by 2, if stones is odd, then stones is also incremented by 2.
  Finally, the function returns the array arr.
*/

// Solution 2
function makeAPile(n) {
  let arr = [];
  let stones = n;

  for (let i = 0; i < n; i++) {
    arr.push(stones);
    stones = stones % 2 === 0 ? stones + 2 : stones + 2;
  }

  return arr;
}

console.log(makeAPile(3)); // [3, 5, 7]

/* 
  Explanation:
  This solution works the same as the first one, but it uses a ternary operator to simplify the if-else statement.
  The ternary operator (stones % 2 === 0 ? stones + 2 : stones + 2) checks if stones is even or odd and returns the