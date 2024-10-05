  if n > m {
    return -1
  }
B:
  avg := math.Round(float64(n+m) / 2)
C:
  return fmt.Sprintf("%b", int(avg))
}

func main() {
  fmt.Println(RoundedAvg(1, 5))
  fmt.Println(RoundedAvg(7, 5))
  fmt.Println(RoundedAvg(10, 20))
  fmt.Println(RoundedAvg(20, 33))
}

