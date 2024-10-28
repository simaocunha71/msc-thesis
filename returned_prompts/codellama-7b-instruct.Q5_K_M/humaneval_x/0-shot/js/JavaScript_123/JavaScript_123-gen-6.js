const getOddCollatz = (n) => {
  let collatz = [n];
  while (n > 1) {
    n = n % 2 === 0 ? n / 2 : 3 * n + 1;
    collatz.push(n);
  }
  return collatz.filter(num => num % 2 !== 0);
}
