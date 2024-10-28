    var result []int
    for i := 0; i < n; i++ {
        var number_stones int
        if i%2 == 0{
            number_stones = i + 1
        }else {
            number_stones = i + 2
        }
        result = append(result, number_stones)
    }
    return result
}



