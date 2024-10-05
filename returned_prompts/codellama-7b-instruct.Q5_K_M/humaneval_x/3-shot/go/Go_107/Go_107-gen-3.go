    var even_count int = 0
    var odd_count int = 0
    for i:=1; i<=n; i++{
        if IsPalindrome(i){
            if IsEven(i){
                even_count += 1
            }else{
                odd_count += 1
            }
        }
    }
    return [2]int{even_count, odd_count}
}

func IsEven(n int) bool{
    return n%2 == 0
}

func IsPalindrome(n int) bool {
    str := strconv.Itoa(n)
    for i := 0; i < len(str); i++ {
        if str[i] != str[len(str)-i-1] {
            return false
        }
    }
    return true
}



