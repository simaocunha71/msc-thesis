func MakeAPile(n int) []int {
  stones := []int{n}
  for i := 1; i < n; i++ {
    if n%2 == 0 {
      stones = append(stones, n+2)
    } else {
      stones = append(stones, n+1)
    }
    n++
  }
  return stones
}