    var sum float64 = 0
    for _, num := range lst {
        sum += math.Pow(math.Ceil(num), 2)
    }
    return int(sum)
}

func main() {
    fmt.Println(SumSquares([]float64{1.4, 4.2, 0}))
    fmt.Println(SumSquares([]float64{-2.4, 1, 1}))
}

