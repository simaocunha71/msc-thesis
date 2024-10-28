  return n % p;
}
// Another way to solve this problem
// const modp = (n, p) => {
//   return (Math.pow(2, n) % p);
// }
// This method is not recommended as it may cause overflow error for large values of n. The first method is safer and more efficient.