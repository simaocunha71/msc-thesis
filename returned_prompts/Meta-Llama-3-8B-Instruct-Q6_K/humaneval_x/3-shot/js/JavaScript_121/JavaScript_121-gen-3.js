  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 2 === 0 && lst[i] % 2 !== 0) {
      sum += lst[i];
    }
  }
  return sum;
}  // or
const solution = (lst) => {
  return lst.filter((x, i) => i % 2 === 0 && x % 2 !== 0).reduce((a, b) => a + b, 0);
}  // or
const solution = (lst) => {
  return lst.reduce((a, x, i) => i % 2 === 0 && x % 2 !== 0 ? a + x : a, 0);
}  // or
const solution = (lst) => {
  return lst.filter(x => x % 2 !== 0).filter((x, i) => i % 2 === 0).reduce((a, b) => a + b, 0);
}  // or
const solution = (lst) => {
  return lst.slice(1).filter((x, i) => i % 2 === 0 && x % 2 !== 0).reduce((a, b) => a + b, 0);
}  // or
const solution = (lst) => {
  return lst.slice(1).reduce((a, x, i) => i % 2 === 0 && x % 2 !== 0 ? a + x : a, 0);
}  // or
const solution = (lst) => {
  let sum = 0;
  for (let i = 1; i < lst.length; i += 2) {
    if (lst[i] % 2 !== 0) {
      sum += lst[i];
    }
  }
  return sum;
}  // or
const solution = (lst) => {
  let sum = 0;
  for (let i = 0; i < lst.length; i += 2) {
    if (lst[i] % 2 !== 0) {
      sum += lst[i];
    }
  }
  return sum;
}  // or
const solution = (lst) => {
  return lst.filter((x, i) => i % 2 === 0).reduce((a, b) => a + b, 0);
}