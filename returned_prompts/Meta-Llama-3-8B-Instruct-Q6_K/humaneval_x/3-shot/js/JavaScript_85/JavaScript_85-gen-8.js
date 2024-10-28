  let sum = 0;
  for (let i = 1; i < lst.length; i += 2) {
    if (lst[i] % 2 === 0) {
      sum += lst[i];
    }
  }
  return sum;
}
// Alternative Solution:
const add = (lst) => {
  return lst.filter((x, i) => i % 2 !== 0 && x % 2 === 0).reduce((a, b) => a + b, 0);
}
// Alternative Solution:
const add = (lst) => {
  return lst.reduce((a, x, i) => i % 2 !== 0 && x % 2 === 0 ? a + x : a, 0);
}