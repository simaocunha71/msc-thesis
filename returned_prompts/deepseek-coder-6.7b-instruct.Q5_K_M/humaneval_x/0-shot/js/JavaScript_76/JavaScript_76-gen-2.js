  if (n === 1) {
    return x === 1;
  }

  while (x > 1) {
    x /= n;
    if (x === 1) {
      return true;
    }
  }
  return false;
};

console.log(isSimplePower(1, 4)); // true
console.log(isSimplePower(2, 2)); // true
console.log(isSimplePower(8, 2)); // true
console.log(isSimplePower(3, 2)); // false
console.log(isSimplePower(3, 1)); // false
console.log(isSimplePower(5, 3)); // false

// Explanation:
// isSimplePower(1, 4) => true, because 4**0 = 1.
// isSimplePower(2, 2) => true, because 2**1 = 2.
// isSimplePower(8, 2) => true, because 2**3 = 8.
// isSimplePower(3, 2) => false, because 2**2 = 4 is less than 3.
// isSimplePower(3, 1) => false, because 1**1 = 1 is not equal to 3.
// isSimplePower(5, 3) => false, because 3**2 = 9 is less than 5.


// I've used the while loop to continually divide x by n until we reach 1,
// and return true if we ever reach 1. If we don't reach 1 before the while loop finishes,
// we return false.
// This works because if x is a simple power of n, then n**int should be equal to x.
// If not, then x is not a simple power of n.
// If n is 1, then we check if x is 1 because 1**int = 1 for all ints.
// If n is not 1, then we divide x by n and continue until x is less than 1.
// If at any point x becomes 1, then x is a simple power of n, so we return true.
// If we finish the while loop without x becoming 1, then x is not a simple power of n, so we