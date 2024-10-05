    count := 0

    for _, num := range nums {
        if num > 10 && isOdd(num) {
            count++
        }
    }

    return count
}

func isOdd(num int) bool {
    str := strconv.Itoa(num)
    firstDigit := str[0]
    lastDigit := str[len(str)-1]

    return firstDigit == '1' || firstDigit == '3' || firstDigit == '5' || firstDigit == '7' || firstDigit == '9' &&
        lastDigit == '1' || lastDigit == '3' || lastDigit == '5' || lastDigit == '7' || lastDigit == '9'
}

// Alternate Solution:

func isOdd(num int) bool {
    str := strconv.Itoa(num)
    firstDigit := str[0]
    lastDigit := str[len(str)-1]

    return firstDigit == '1' || firstDigit == '3' || firstDigit == '5' || firstDigit == '7' || firstDigit == '9' &&
        lastDigit == '1' || lastDigit == '3' || lastDigit == '5' || lastDigit == '7' || lastDigit == '9'
}

func Specialfilter(nums []int) int {
    count := 0

    for _, num := range nums {
        if num > 10 && isOdd(num) {
            count++
        }
    }

    return count
}

// Alternate Solution:

func isOdd(num int) bool {
    str := strconv.Itoa(num)
    firstDigit := str[0]
    lastDigit := str[len(str)-1]

    return firstDigit == '1' || firstDigit == '3' || firstDigit == '5' || firstDigit == '7' || firstDigit == '9' &&
        lastDigit == '1' ||