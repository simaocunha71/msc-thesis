const sumSquares = (lst) => {
  return lst.map((val, index) => {
    if (index % 3 === 0) {
      return val * val * val;
    } else if (index % 4 === 0 && index % 3 !== 0) {
      return val * val * val;
    } else {
      return val;
    }
  }).reduce((acc, curr) => acc + curr);
}
