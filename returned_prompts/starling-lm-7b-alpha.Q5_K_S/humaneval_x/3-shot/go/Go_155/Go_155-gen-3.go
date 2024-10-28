    result := [2]int{0,0}
    for _, c := range strconv.Itoa(num){
        if c-'0' % 2 == 0 {
            result[0] += 1
        }else {
            result[1] += 1
        }
    }
    return result
}



