  let min = Math.min(...numbers);
  let max = Math.max(...numbers);
  return numbers.map(num => (num - min) / (max - min));
}
// or
const rescaleToUnit = (numbers) => {
  let min = Math.min(...numbers);
  let max = Math.max(...numbers);
  return numbers.map(num => (num - min) / (max - min));
}  // This one is for ES6 or later versions. For ES5 and earlier versions, you should use the first solution.