    sum := 0
    for _,num := range q {
        sum += num
    }
    return sum <= w && isPalindrome(q)
}

func isPalindrome(slice []int) bool {
    left,right := 0,len(slice)-1
    for left < right {
        if slice[left] != slice[right] {
            return false
        }
        left += 1
        right -= 1
    }
    return true
}



