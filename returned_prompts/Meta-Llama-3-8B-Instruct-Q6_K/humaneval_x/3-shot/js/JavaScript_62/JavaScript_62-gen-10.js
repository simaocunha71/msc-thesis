  let result = [xs[1]];
  for (let i = 2; i < xs.length; i++) {
    result.push((i + 1) * xs[i]);
  }
  return result;
}
//or
const derivative = (xs) => {
  return xs.slice(1).map((x, i) => (i + 1) * x);
}  // using map and slice
//or
const derivative = (xs) => {
  return xs.slice(1).map((x, i) => i * x);
}  // using map and slice, for the constant term 0
//or
const derivative = (xs) => {
  return xs.slice(1).map((x, i) => (i + 1) * x).reduce((a, b) => a + b, 0);
}  // using map, reduce and slice
//or
const derivative = (xs) => {
  return xs.slice(1).map((x, i) => (i + 1) * x).reduce((a, b) => a + b, 0);
}  // using map, reduce and slice, for the constant term 0
//or
const derivative = (xs) => {
  return xs.slice(1).map((x, i) => (i + 1) * x).reduce((a, b) => a + b, 0);
}  // using map, reduce and slice, for the constant term 0
//or
const derivative = (xs) => {
  return xs.slice(1).map((x, i) => (i + 1) * x).reduce((a, b) => a + b, 0);
}  // using map, reduce and slice, for the constant term 0
//or
const derivative = (xs) => {
  return xs.slice(1).map((x, i) => (i + 1) * x).reduce((a, b) => a + b, 0);
}  // using map, reduce and slice, for the constant term 0
//or
const derivative = (xs) => {
  return xs.slice(1).map((x, i) => (i + 1) * x).reduce((a, b) => a + b, 0);
}  // using map, reduce and slice, for the constant term