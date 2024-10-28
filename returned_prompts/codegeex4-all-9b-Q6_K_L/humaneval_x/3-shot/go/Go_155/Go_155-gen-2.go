    num_str := strconv.Itoa(num)
    var count [2]int
    for _, c := range num_str {
        if c % 2 == 0 {
            count[0] += 1
        }else{
            count[1] += 1
        }
    }
    return count
}

