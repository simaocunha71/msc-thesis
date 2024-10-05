    sort.Slice(arr, func(i, j int) bool {
        a, b := arr[i], arr[j]
        aOnes, bOnes := 0, 0
        for a > 0 {
            aOnes += a % 2
            a /= 2
        }
        for b > 0 {
            bOnes += b % 2
            b /= 2
        }
        return aOnes < bOnes || (aOnes == bOnes && arr[i] < arr[j])
    })
    return arr
}



