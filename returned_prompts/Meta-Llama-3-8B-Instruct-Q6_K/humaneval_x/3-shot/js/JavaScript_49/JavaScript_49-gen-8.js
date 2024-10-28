  return n % p;
}  // This is the simplest way, but it may not work for large numbers due to numeric limitations.
  // To handle large numbers, you can use the pow function.
  // return Math.pow(n, p) % p;  // This will give the same result as above, but it might work for larger numbers.
}  // Note that the second parameter should be a prime number to avoid ambiguity.
  // For example, modp(3, 4) could be 3 or 1, so it's not a valid mod operation.
}  // You can also use a library like BigInteger if you need to handle very large numbers.