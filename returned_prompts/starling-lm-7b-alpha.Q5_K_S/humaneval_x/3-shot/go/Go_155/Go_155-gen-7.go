    result := [2]int{}
    count_even := 0
    count_odd := 0
    for n := strconv.Itoa(num); len(n) > 0; n = n[:len(n)-1] {
        if len(n) == 0 {
            break
        }
        if n[0] == '0' {
            count_even += 1
        }else if n[0] == '1' {
            count_odd += 1
        }else if n[0] == '2' || n[0] == '3' || n[0] == '4' || n[0] == '5' || n[0] == '6' || n[0] == '7' || n[0] == '8' || n[0] == '9' {
            count_odd += 1
        }
    }
    result[0] = count_even
    result[1] = count_odd
    return result
}



