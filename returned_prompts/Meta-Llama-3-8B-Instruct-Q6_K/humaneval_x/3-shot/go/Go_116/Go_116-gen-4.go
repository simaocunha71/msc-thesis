    type pair struct {
        num int
        ones int
    }

    sort.Slice(arr, func(i, j int) bool {
        p1 := pair{arr[i], binaryLength(arr[i])}
        p2 := pair{arr[j], binaryLength(arr[j])}
        if p1.ones != p2.ones {
            return p1.ones < p2.ones
        }
        return p1.num < p2.num
    })

    return arr
}

func binaryLength(n int) int {
    count := 0
    for n > 0 {
        n >>= 1
        count++
    }
    return count
}