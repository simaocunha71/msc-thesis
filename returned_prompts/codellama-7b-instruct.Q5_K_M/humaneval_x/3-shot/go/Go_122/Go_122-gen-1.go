    sum := 0
    for i := 0; i < k; i++ {
        if len(strconv.Itoa(arr[i])) <= 2 {
            sum += arr[i]
        }
    }
    return sum
}


