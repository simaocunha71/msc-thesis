func HowManyTimes(str string, substring string) int {
  if len(str) == 0 || len(substring) == 0 {
    return 0
  }
  count := 0
  for i := 0; i < len(str); i++ {
    if str[i:i+len(substring)] == substring {
      count++
    }
  }
  return count
}

func main() {
  fmt.Println(HowManyTimes("a", "a")) // 1
  fmt.Println(HowManyTimes("aaa", "a")) // 3
  fmt.Println(HowManyTimes("aaaa", "aa")) // 3
  fmt.Println(HowManyTimes("aaaa", "aaa")) // 2
  fmt.Println(HowManyTimes("aaaa", "aaaa")) // 1
  fmt.Println(HowManyTimes("aaaa", "aaaaa")) // 0
}