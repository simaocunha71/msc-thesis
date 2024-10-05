    var result []int
    for _, num := range arr {
        result = append(result, num)
    }
    sort.Slice(result, func(i, j int) bool {
        s1 := fmt.Sprintf("%b", result[i])
        s2 := fmt.Sprintf("%b", result[j])
        count1 := 0
        count2 := 0
        for _, v := range s1 {
            if v == '1' {
                count1++
            }
        }
        for _, v := range s2 {
            if v == '1' {
                count2++
            }
        }
        if count1 == count2 {
            return result[i] < result[j]
        }
        return count1 < count2
    })

    return result
}



