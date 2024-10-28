func Monotonic(l []int) bool {
  if len(l) < 2 {
    return true
  }
  isIncreasing := l[0] < l[1]
  for i := 1; i < len(l); i++ {
    if (l[i-1] < l[i]) != isIncreasing {
      return false
    }
  }
  return true
}