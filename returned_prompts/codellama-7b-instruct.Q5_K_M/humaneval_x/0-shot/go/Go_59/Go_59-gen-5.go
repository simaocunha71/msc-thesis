
// Return the largest prime factor of n. Assume n > 1 and is not a prime.
// >>> LargestPrimeFactor(13195)
// 29
// >>> LargestPrimeFactor(2048)
// 2
func LargestPrimeFactor(n int) int {
  if n == 1 {
    return 1
  }
  if n % 2 == 0 {
    return LargestPrimeFactor(n / 2)
  }
  for i := 3; i*i <= n; i += 2 {
    if n % i == 0 {
      return LargestPrimeFactor(n / i)
    }
  }
  return n
}
