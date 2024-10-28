    num_str := strconv.Itoa(num)
    var even_count, odd_count int

    for _, c := range num_str {
        if c % 2 == 0 {
            even_count += 1
        }else{
            odd_count += 1
        }
    }
    return [2]int{even_count, odd_count}
}



