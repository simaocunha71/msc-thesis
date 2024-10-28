    sort.Slice(arr, func(i, j int) bool {
        a, b := arr[i], arr[j]
        aCount, bCount := bits.OnesCount(uint(a)), bits.OnesCount(uint(b))
        if aCount == bCount {
            return a < b
        }
        return aCount < bCount
    })
    return arr
}



