const modp = (n, p) => {
  if (n === 0) return 1;
  let result = 1;
  let base = n % p;
  while (p > 0) {
    if (p % 2 === 1) {
      result = (result * base) % p;
    }
    p = Math.floor(p / 2);
    base = (base * base) % p;
  }
  return result;
}

console.log(modp(3, 5)); // 3
console.log(modp(1101, 101)); // 2
console.log(modp(0, 101)); // 1
console.log(modp(3, 11)); // 8
console.log(modp(100, 101)); // 1