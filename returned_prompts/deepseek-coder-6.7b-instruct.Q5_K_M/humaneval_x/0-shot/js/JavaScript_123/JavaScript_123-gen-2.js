  let collatz = [n];
  while (n != 1) {
    if (n % 2 != 0) {
      collatz.push(n);
    }
    n = n % 2 === 0 ? n / 2 : 3 * n + 1;
  }
  return collatz.sort((a, b) => a - b);
}

console.log(getOddCollatz(5)) // [1, 5]
console.log(getOddCollatz(11)) // [1, 11, 22, 44]
console.log(getOddCollatz(26)) // [1, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2]
console.log(getOddCollatz(57)) // [1, 57, 172, 86, 43, 140, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2]

// Explanation:
// The Collatz sequence for 5 is [5, 16, 8, 4, 2, 1]. The odd numbers are [5, 1], so [1, 5] is returned.
// The Collatz sequence for 11 is [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]. The odd numbers are [11, 34, 17, 52, 26, 13, 40, 20, 10, 16, 8, 4, 2], so [1, 11, 22, 44] is returned.
// The Collatz sequence for 26 is [26, 13, 40, 