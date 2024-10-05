
const isEqualToSumEven = (n) => {
  for (let i = 2; i <= n; i++) {
    if ((n - i) % 2 === 0) {
      return true
    }
  }
  return false
}
