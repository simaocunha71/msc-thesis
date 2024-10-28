
    if len(lst1) == 0 {
        return "NO"
    }
    // Count odd numbers in lst1
    oddCount := 0
    for _, v := range lst1 {
        if v%2 != 0 {
            oddCount++
        }
    }

    // If oddCount is greater than the length of lst2, it's impossible to exchange
    if oddCount > len(lst2) {
        return "NO"
    }

    // If oddCount is less than or equal to the length of lst2, we can still try to exchange
    for _, v := range lst1 {
        if v%2 != 0 {
            for _, u := range lst2 {
                if u%2 != 0 {
                    lst1[findIndex(lst1, v)], lst2[findIndex(lst2, u)] = lst2[findIndex(lst2, u)], lst1[findIndex(lst1, v)]
                    break
                }
            }
        }
    }

    for _, v := range lst1 {
        if v%2 != 0 {
            return "NO"
        }
    }
    return "YES"
}

func findIndex(arr []int, v int) int {
    for i, e := range arr {
        if e == v {
            return i
        }
    }
    return -1
}



// Here is a simple implementation of the Exchange function in Go.
// This function first checks if the length of lst1 is 0, if so, it returns "NO".
// Then it counts the number of odd numbers in lst1.
// If the number of odd numbers is greater than the length of lst2, it is impossible to exchange, so it returns "NO".
// If the number of odd numbers is less than or equal to the length of lst2, it continues to exchange the odd numbers in lst1 and lst2.
// After the exchange, it checks if there are still odd numbers in lst1, if so, it returns "NO".
// If all the elements in lst1 are even, it returns