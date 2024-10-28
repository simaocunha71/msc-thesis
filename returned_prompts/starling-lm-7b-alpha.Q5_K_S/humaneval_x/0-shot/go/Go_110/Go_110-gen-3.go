
    // Count the number of odd and even elements in lst1 and lst2
    oddCnt := 0
    evenCnt := 0
    for _, v := range lst1 {
        if v%2 != 0 {
            oddCnt++
        } else {
            evenCnt++
        }
    }
    for _, v := range lst2 {
        if v%2 != 0 {
            oddCnt++
        } else {
            evenCnt++
        }
    }

    // If the total number of odd elements is less than or equal to the total number of even elements in lst1,
    // then it is possible to make lst1 a list of only even numbers.
    if oddCnt <= len(lst1)-evenCnt {
        return "YES"
    }

    // Otherwise, return "NO".
    return "NO"
}




func Exchange(lst1, lst2 []int) string {
    oddCnt := 0
    evenCnt := 0
    for _, v := range lst1 {
        if v%2 != 0 {
            oddCnt++
        } else {
            evenCnt++
        }
    }
    for _, v := range lst2 {
        if v%2 != 0 {
            oddCnt++
        } else {
            evenCnt++
        }
    }
    if oddCnt <= len(lst1)-evenCnt {
        return "YES"
    }
    return "NO"
}












































































































































