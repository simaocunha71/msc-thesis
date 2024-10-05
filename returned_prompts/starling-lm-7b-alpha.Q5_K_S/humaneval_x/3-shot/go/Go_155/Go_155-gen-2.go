    result := [2]int{0,0}
    for _,c := range strconv.Itoa(num){
        if c == '0' || c == '2' || c == '4' || c == '6' || c == '8' {
            result[0] += 1
        }else if c == '1' || c == '3' || c == '5' || c == '7' || c == '9' {
            result[1] += 1
        }
    }
    return result
}



