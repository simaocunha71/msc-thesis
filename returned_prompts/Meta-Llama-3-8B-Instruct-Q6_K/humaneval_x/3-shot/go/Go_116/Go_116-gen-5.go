    type pair struct {
        val int
        one int
    }

    sort.Slice(arr, func(i, j int) bool {
        if arr[i] < arr[j] {
            return true
        }
        if arr[i] > arr[j] {
            return false
        }
        ones1 := 0
        for ; arr[i] > 0; arr[i] /= 2 {
            ones1++
        }
        ones2 := 0
        for ; arr[j] > 0; arr[j] /= 2 {
            ones2++
        }
        return ones1 < ones2
    })
    return arr
}