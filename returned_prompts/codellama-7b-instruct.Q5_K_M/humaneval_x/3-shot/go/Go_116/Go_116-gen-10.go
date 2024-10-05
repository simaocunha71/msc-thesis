    var sorted []int
    var ones []int

    for _, num := range arr {
        var binary_num []int
        var binary_str string
        binary_str = fmt.Sprintf("%b", num)
        for _, bit := range binary_str {
            if bit == '1'{
                binary_num = append(binary_num, 1)
            }else{
                binary_num = append(binary_num, 0)
            }
        }
        ones = append(ones, binary_num...)
    }

    sort.Ints(ones)
    for _, num := range ones {
        if num == 0 {
            sorted = append(sorted, 0)
        }else{
            for _, num_ := range arr {
                if num_ == num{
                    sorted = append(sorted, num_)
                    break
                }
            }
        }
    }
    return sorted
}



