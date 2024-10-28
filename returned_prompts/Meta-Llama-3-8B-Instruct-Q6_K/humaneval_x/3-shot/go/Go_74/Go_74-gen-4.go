    var result []string
    minSum := math.MaxFloat64
    var minSumList []string

    if sum1 := sumChars(lst1); sum1 < minSum {
        minSum = sum1
        minSumList = lst1
    }

    if sum2 := sumChars(lst2); sum2 < minSum {
        minSum = sum2
        minSumList = lst2
    }

    return minSumList

}

func sumChars(lst []string) float64 {
    sum := 0.0
    for _, v := range lst {
        sum += float64(len([]byte(v)))
    }
    return sum
}