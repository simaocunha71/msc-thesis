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
    let stack = [n];
    let res = [n];
    for (let i = 1; i < n; i++) {
      let x = stack.pop();
      if (x % 2 === 0) {
        stack.push(x + 2);
        stack.push(x + 1);
      } else {
        stack.push(x + 1);
        stack.push(x + 2);
      }
      res.push(x);
    }
    return res;
  };

  let n = 4;
  console.log(makeAPile(n));

  //?
  let n = 3;
  console.log(makeAPile(n));

  //*
  let n = 5;
  console.log(makeAPile(n));

  //?
  let n = 6;
  console.log(makeAPile(n));

  //*
  let n = 7;
  console.log(makeAPile(n));

  //?
  let n = 8;
  console.log(makeAPile(n));

  //*
  let n = 9;
  console.log(makeAPile(n));

  //?
  let n = 10;
  console.log(makeAPile(n));

  //*
  let n = 11;
  console.log(makeAPile(n));

  //?
  let n = 12;
  console.log(make