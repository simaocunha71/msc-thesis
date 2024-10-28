  var result = 0;
  var odd_squares = [];
  for (const x of lst) {
    if (Math.round(x) == x && x >= 0) {
      odd_squares.push(x * x);
    }
  }
  result = odd_squares.reduce((a, b) => a + b, 0);
  return result;
}



