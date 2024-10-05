
func GenerateIntegers(a, b int) []int {
    var result []int
    for i := a; i <= b; i++ {
        digits := strconv.Itoa(i)
        for _, char := range digits {
            if (char-'0')%2 == 0 {
                result = append(result, char-'0')
            }
        }
    }
    sort(result)
    return result
}




func GenerateIntegers(a, b int) []int {
    result := []int{}
    for i := a; i <= b; i++ {
        s := strconv.Itoa(i)
        for _, r := range s {
            if r%2 == 0 {
                result = append(result, int(r))
            }
        }
    }
    sort(result)
    return result
}



func GenerateIntegers(a, b int) []int {
    result := []int{}
    for i := a; i <= b; i++ {
        s := strconv.Itoa(i)
        for _, r := range s {
            if r%2 == 0 {
                result = append(result, int(r))
            }
        }
    }
    sort(result)
    return result
}



func GenerateIntegers(a, b int) []int {
    result := []int{}
    for i := a; i <= b; i++ {
        s := strconv.Itoa(i)
        for _, r := range s {
            if r%2 == 0 {
                result = append(result, int(r))
            }
        }
    }
    sort(result)
    return result
}








func GenerateIntegers(a, b int) []int {
    result := []int{}
    for i := a; i <= b; i++ {
        s := strconv.Itoa(i)
        for _, r := range s {
            if r%2 == 0 {
                result = append(result, int(