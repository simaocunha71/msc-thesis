    type pair struct {
        num int
        ones int
    }

    sort.Slice(arr, func(i, j int) bool {
        if arr[i] == arr[j] {
            return arr[i] < arr[j]
        }
        count1 := 0
        for ; arr[i] > 0; arr[i] /= 2 {
            if arr[i]%2 == 1 {
                count1++
            }
        }
        count2 := 0
        for ; arr[j] > 0; arr[j] /= 2 {
            if arr[j]%2 == 1 {
                count2++
            }
        }
        if count1 != count2 {
            return count1 < count2
        }
        return false
    })
    return arr
}