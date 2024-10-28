  return Math.log(x) / Math.log(n) % 1 === 0;
}
// or
const isSimplePower = (x, n) => {
  return Math.pow(n, Math.floor(Math.log(x) / Math.log(n))) === x;
}
// or
const isSimplePower = (x, n) => {
  let i = 1;
  while (Math.pow(n, i) <= x) {
    if (Math.pow(n, i) === x) {
      return true;
    }
    i++;
  }
  return false;
}