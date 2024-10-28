  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 2 === 0 && lst[i] % 2 !== 0) {
      sum += lst[i];
    }
  }
  return sum;
}
// Another way
const solution = (lst) => {
  return lst.filter((x, i) => i % 2 === 0 && x % 2 !== 0).reduce((a, b) => a + b, 0);
}
// Another way
const solution = (lst) => {
  return lst.reduce((a, x, i) => i % 2 === 0 && x % 2 !== 0 ? a + x : a, 0);
}
// Another way
const solution = (lst) => {
  return lst.filter(x => x % 2 !== 0).filter((x, i) => i % 2 === 0).reduce((a, b) => a + b, 0);
}
// Another way
const solution = (lst) => {
  return lst.reduce((a, x) => x % 2 === 0 && x % 2 !== 0 ? a + x : a, 0);
}  // Another way
const solution = (lst) => {
  return lst.filter(x => x % 2 !== 0).map(x => x).filter((x, i) => i % 2 === 0).reduce((a, b) => a + b, 0);
}
// Another way
const solution = (lst) => {
  return lst.filter(x => x % 2 !== 0).map(x => x).reduce((a, b) => a + b, 0);
}
// Another way
const solution = (lst) => {
  return lst.filter(x => x % 2 !== 0).reduce((a, b) => a + b, 0);
}
// Another way
const solution = (lst) => {
  return lst.filter(x => x % 2 !== 0).reduce((a, b) => a + b, 0);
}
// Another way
const solution = (lst) => {
  return lst.filter(x => x % 2 !== 0).reduce((a, b) => a + b, 0);
}
// Another way
const solution = (lst) => {
 