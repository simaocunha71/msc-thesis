    type pair struct {
        val  int
        ones int
    }
    result := make([]int, 0)
    for _,v := range arr {
        result = append(result, v)
    }
    sort.Slice(result, func(i int, j int) bool {
        i_one := 0
        j_one := 0
        for {
            if result[i] < 0 {
                break
            }
            i_one += result[i]%2
            result[i]/=2
            if result[j] < 0 {
                break
            }
            j_one += result[j]%2
            result[j]/=2
        }
        return i_one < j_one || i_one == j_one && result[i] < result[j]
    })
    return result
}



