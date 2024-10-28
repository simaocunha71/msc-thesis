const simplify = (x, n) => {
  return ((x * n).split('/')[1] === '1');
}

B:
const simplify = (x, n) => {
  return ((x * n).split('/')[0] % 1 === 0);
}

C:
const simplify = (x, n) => {
  let [a, b] = x.split('/');
  let [c, d] = n.split('/');
  return a * d === b * c;
}

D:
const simplify = (x, n) => {
  let [a, b] = x.split('/');
  let [c, d] = n.split('/');
  return a % d === 0 && b % c === 0;
}
