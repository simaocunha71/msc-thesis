
return [2]int{evenCount, oddCount}
}


B:

func EvenOddCount(num int) [2]int {
    evenCount := 0
    oddCount := 0
    for ; num > 0; num /= 10 {
        if num % 10 % 2 == 0 {
            evenCount++
        } else {
            oddCount++
        }
    }
    return [2]int{evenCount, oddCount}
}


C:

func EvenOddCount(num int) (even int, odd int) {
    for ; num > 0; num /= 10 {
        if num % 10 % 2 == 0 {
            even++
        } else {
            odd++
        }
    }
    return
}


D:

func EvenOddCount(num int) (even int, odd int) {
    for ; num > 0; num /= 10 {
        if num % 2 == 0 {
            even++
        } else {
            odd++
        }
    }
    return
}