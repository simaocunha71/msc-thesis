    sum := 0
    cnt := 0
    for _, v := range arr {
        sum = 0
        for i := 0; i < len(strconv.Itoa(abs(v))); i++ {
            sum += int(strconv.Itoa(abs(v))[i])
        }
        if sum > 0 {
            cnt++
        }
    }
    return cnt
}



// The function CountNums is incorrect, please correct it.
// >>> CountNums([]) == 0
// >>> CountNums([-1, 11, -11]) == 2
// >>> CountNums([1, 1, 2]) == 3
func CountNums(arr []int) int {
    sum := 0
    cnt := 0
    for _, v := range arr {
        sum = 0
        for _, v := range strconv.Itoa(abs(v)) {
            sum += int(v)
        }
        if sum > 0 {
            cnt++
        }
    }
    return cnt
}






func CountNums(arr []int) int {
    sum := 0
    cnt := 0
    for _, v := range arr {
        sum = 0
        for i := 0; i < len(strconv.Itoa(abs(v))); i++ {
            sum += int(strconv.Itoa(abs(v))[i])
        }
        if sum > 0 {
            cnt++
        }
    }
    return cnt
}






func CountNums(arr []int) int {
    sum := 0
    cnt := 0
    for _, v := range arr {
        sum = 0
        for i := 0; i < len(strconv.Itoa(abs(v))); i++ {
            sum += int(strconv.Itoa(abs(v))[i])
        }
        if sum > 0 {
            cnt++
        }
    }
    return cnt
}
















