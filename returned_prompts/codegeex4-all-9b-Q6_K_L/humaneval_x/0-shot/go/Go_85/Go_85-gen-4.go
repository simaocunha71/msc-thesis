func Add(lst []int) int {
  s := 0
  for i := 1; i < len(lst); i += 2 {
    if lst[i] % 2 == 0 {
      s += lst[i]
    }
  }
  return s
}