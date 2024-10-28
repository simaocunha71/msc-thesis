const rollingMax = (numbers) => numbers.map(
  (num, i, arr) => arr.slice(0, i + 1).reduce((acc, curr) => Math.max(acc, curr), num)
);

// https://stackoverflow.com/questions/35051394/javascript-reduce-vs-map-vs-foreach
// https://www.freecodecamp.org/news/reduce-f47a7f55ae63/
