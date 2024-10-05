func LargestPrimeFactor(n int) int {
  i := 2
  for i <= n {
    if n%i == 0 {
      n /= i
    } else {
      i++
    }
  }
  return i - 1
}