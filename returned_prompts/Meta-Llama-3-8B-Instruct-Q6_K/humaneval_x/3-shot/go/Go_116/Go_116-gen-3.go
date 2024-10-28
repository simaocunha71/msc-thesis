    type pair struct {
        num int
        ones int
    }

    sort.Slice(arr, func(i, j int) bool {
        a := pair{num: arr[i], ones: binCount(arr[i])}
        b := pair{num: arr[j], ones: binCount(arr[j])}
        if a.ones != b.ones {
            return a.ones < b.ones
        }
        return a.num < b.num
    })

    return arr
}

func binCount(n int) int {
    count := 0
    for n > 0 {
        n = n & (n - 1)
        count++
    }
    return count
}
}