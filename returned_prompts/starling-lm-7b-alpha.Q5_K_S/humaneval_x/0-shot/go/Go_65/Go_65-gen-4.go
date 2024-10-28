
var result int
var y int
var i int
var digits []int

if shift > 0 {
    result = x

    digits = make([]int, 0)
    y = x
    for y != 0 {
        digits = append(digits, y%10)
        y /= 10
    }

    for i = 0; i < len(digits) && i < shift; i++ {
        result *= 10
        result += digits[len(digits)-1-i]
    }

    if len(digits) > shift {
        result += digits[0]
        for i = 1; i < len(digits)-shift; i++ {
            result *= 10
            result += digits[i]
        }
    } else {
        for i = 0; i < len(digits); i++ {
            result *= 10
            result += digits[i]
        }
    }
} else {
    result = x
}

return strconv.Itoa(result)
}
























































































































































































































































