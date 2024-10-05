  var factors = [];
  while (n > 1) {
    for (let i = 2; i <= n; i++) {
      if (n % i == 0) {
        factors.push(i);
        n = n / i;
        break;
      }
    }
  }
  return factors;
}

This function takes an integer n and returns an array of prime factors of n. The array should contain each prime factor of n, repeated as many times as it appears in the prime factorization of n.
For example, factorize(8) should return [2, 2, 2] because 8 is equal to 2 * 2 * 2.
factorize(25) should return [5, 5] because 25 is equal to 5 * 5.
factorize(70) should return [2, 5, 7] because 70 is equal to 2 * 5 * 7.
The function uses a while loop to keep dividing n by prime factors until n is equal to 1. For each iteration of the while loop, the function uses a for loop to check if i is a prime factor of n. If i is a prime factor of n, the function adds i to the factors array and divides n by i. This process continues until n is equal to 1. The function then returns the factors array.