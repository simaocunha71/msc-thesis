    var sum float64 = 0

B:
    for i := 0; i < len(lst); i++ {
        if lst[i] > 0 && math.Mod(lst[i], 2) != 0 {
            sum += math.Pow(lst[i], 2)
        }
    }

C:
    return int(sum)
}

func main() {
    fmt.Println(DoubleTheDifference([]float64{1, 3, 2, 0})) // 10
    fmt.Println(DoubleTheDifference([]float64{-1, -2, 0}))  // 0
    fmt.Println(DoubleTheDifference([]float64{9, -2}))      // 81
    fmt.Println(DoubleTheDifference([]float64{0}))           // 0
    fmt.Println(DoubleTheDifference([]float64{}))            // 0
}


