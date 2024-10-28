    digits := []int{}
    str := strconv.Itoa(x)
    for _, c := range str {
        digits = append(digits, int(c-'0'))
    }
    shift = shift % len(digits)
    if shift == 0 {
        return strconv.Itoa(x)
    }
    return strconv.Itoa(reverse(digits, shift))
}

func reverse(a []int, n int) int {
    result := 0
    for i := 0; i < n; i++ {
        result = result*10 + a[len(a)-1-i]
    }
    return result
}