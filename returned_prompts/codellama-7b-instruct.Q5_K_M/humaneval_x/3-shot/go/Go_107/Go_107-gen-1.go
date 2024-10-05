    even := 0
    odd := 0

    for i := 1; i < n; i++ {
        if isPalindrome(i){
            if isEven(i){
                even += 1
            }else{
                odd += 1
            }
        }
    }

    return [2]int{even, odd}
}

func isEven(n int) bool {
    return strconv.Itoa(n) == strconv.Itoa(n)[::-1]
}

func isPalindrome(n int) bool {
    return strconv.Itoa(n) == strconv.Itoa(n)[::-1]
}



