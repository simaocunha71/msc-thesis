    num_str := strconv.Itoa(num)
    var result [2]int
    for _, c := range num_str{
        if c%2 == 0 {
            result[0] += 1
        }else{
            result[1] += 1
        }
    }
    return result
}



