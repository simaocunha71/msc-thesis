    result := 0
    n := len(arr)
    for i := 0; i < n / 2; i++ {
        if arr[i] != arr[n-1-i] {
            result += 1
        }
    }
    if n % 2 == 1 {
        result += 1 - (arr[n/2] % 2)
    }
    return result / 2
}



