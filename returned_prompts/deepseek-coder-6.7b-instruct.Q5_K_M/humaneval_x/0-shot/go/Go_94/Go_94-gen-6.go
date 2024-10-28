  for _, v := range lst {
    if v < 2 {
      continue A
    }
    for i := 2; i*i <= v; i++ {
      if v%i == 0 {
        goto A
      }
    }
    s := 0
    for v > 0 {
      s += v % 10
      v /= 10
    }
    return s
  }
  return 0
}

func main() {
    fmt.Println(Skjkasdkd([0,3,2,1,3,5,7,4,