    evenCount := 0
    oddCount := 0

    num_str := strconv.Itoa(abs(num))
    for _, c := range num_str {
        digit, _ := strconv.Atoi(string(c))
        if digit%2 == 0 {
            evenCount++
        } else {
            oddCount++
        }
    }

    return [2]int{evenCount, oddCount}
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
} 





