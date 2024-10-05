  let min = Math.min(...numbers);
  let max = Math.max(...numbers);
  let scale = 1.0 / (max - min);

  return numbers.map((num) => (num - min) * scale);
}
// Another way to do it
const rescaleToUnit = (numbers) => {
  let min = Math.min(...numbers);
  let max = Math.max(...numbers);
  let scale = 1.0 / (max - min);

  return numbers.map((num) => (num - min) * scale).map((num) => parseFloat(num.toFixed(10)));
}