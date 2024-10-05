    n := len(arr)
    count := 0
    for i := 0; i < n / 2; i++ {
        if arr[i] != arr[n-i-1] {
            count++
        }
    }
    if n % 2 == 1 {
        if arr[n/2] % 2 == 0 {
            count++
        }
    }
    return count
}



