    count := 0
    for _, v := range nums {
        i := strconv.Itoa(v)
        if len(i) <= 1 {
            continue
        }
        if i[0] == '1' || i[0] == '3' || i[0] == '5' || i[0] == '7' || i[0] == '9' {
            if i[len(i)-1] == '1' || i[len(i)-1] == '3' || i[len(i)-1] == '5' || i[len(i)-1] == '7' || i[len(i)-1] == '9' {
                count++
            }
        }
    }
    return count
}



func Specialfilter(nums []int) int {
    count := 0
    for _, v := range nums {
        i := strconv.Itoa(v)
        if len(i) <= 1 {
            continue
        }
        if i[0] == '1' || i[0] == '3' || i[0] == '5' || i[0] == '7' || i[0] == '9' {
            if i[len(i)-1] == '1' || i[len(i)-1] == '3' || i[len(i)-1] == '5' || i[len(i)-1] == '7' || i[len(i)-1] == '9' {
                count++
            }
        }
    }
    return count
}




func Specialfilter(nums []int) int {
    count := 0
    for _, v := range nums {
        i := strconv.Itoa(v)
        if len(i) <= 1 {
            continue
        }
        if i[0] == '1' || i[0] == '3' || i[0] == '5' || i[0] == '7' || i[0] == '9' {
            if i[len(i)-1] == '1' || i[len(i)-1]