const isSimplePower = (x, n) => {
  let power = 1;
  while (power <= x) {
    if (power === x) {
      return true;
    }
    power *= n;
  }
  return false;
}

console.log(isSimplePower(1, 4)) // true
console.log(isSimplePower(2, 2)) // true
console.log(isSimplePower(8, 2)) // true
console.log(isSimplePower(3, 2)) // false
console.log(isSimplePower(3, 1)) // false
console.log(isSimplePower(5, 3)) // false