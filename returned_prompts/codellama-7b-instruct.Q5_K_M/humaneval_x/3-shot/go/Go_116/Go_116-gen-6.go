    result := make([]int, len(arr))
    copy(result, arr)
    sort.Slice(result, func(i, j int) bool {
        i_ones := count_ones(result[i])
        j_ones := count_ones(result[j])
        if i_ones != j_ones {
            return i_ones < j_ones
        }
        return result[i] < result[j]
    })
    return result
}

func count_ones(n int) int {
    ones := 0
    for n > 0 {
        ones += n % 10
        n /= 10
    }
    return ones
}



