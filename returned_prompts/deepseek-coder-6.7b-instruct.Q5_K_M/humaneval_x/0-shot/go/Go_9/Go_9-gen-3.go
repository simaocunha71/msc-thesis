    maxs := make([]int, len(numbers))
    max := math.MinInt64

    for i, num := range numbers {
        if num > max {
            max = num
        }
        maxs[i] = max
    }
    return maxs
}

func main() {
    fmt.Println(RollingMax([]int{1, 2, 3, 2, 3, 4, 2}))
}

