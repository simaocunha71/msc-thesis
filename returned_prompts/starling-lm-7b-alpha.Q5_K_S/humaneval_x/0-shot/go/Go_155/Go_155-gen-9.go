    var even, odd int

    for num != 0 {
        if num % 10 % 2 == 0 {
            even++
        } else {
            odd++
        }
        num /= 10
    }

    return [2]int{even, odd}
}

// Another solution
func EvenOddCount(num int) (int, int) {
    even, odd := 0, 0
    for num != 0 {
        if num % 10 % 2 == 0 {
            even++
        } else {
            odd++
        }
        num /= 10
    }
    return even, odd
}

// Another solution
func EvenOddCount(num int) [2]int {
    return [2]int{
        countEven(num),
        countOdd(num),
    }
}

func countEven(num int) int {
    even := 0
    for num != 0 {
        if num % 10 % 2 == 0 {
            even++
        }
        num /= 10
    }
    return even
}

func countOdd(num int) int {
    odd := 0
    for num != 0 {
        if num % 10 % 2 == 0 {
        } else {
            odd++
        }
        num /= 10
    }
    return odd
}

// Yet another solution
func EvenOddCount(num int) (int, int) {
    var even, odd int
    for num != 0 {
        if num % 10 % 2 == 0 {
            even++
        } else {
            odd++
        }
        num /= 10
    }
    return even, odd
}

// Yet another solution
func EvenOddCount(num int) (int, int) {
    var even, odd int
    for num != 0 {
        if num % 10 % 2 == 0 {
            even++
        } else {
            odd++
        }
        num /= 10
    }
   