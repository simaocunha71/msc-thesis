    if _, ok := x.(int); !ok {
        return false
    }
    if _, ok := y.(int); !ok {
        return false
    }
    if _, ok := z.(int); !ok {
        return false
    }

    if x.(int)+y.(int) == z.(int) {
        return true
    }
    if x.(int)+z.(int) == y.(int) {
        return true
    }
    if y.(int)+z.(int) == x.(int) {
        return true
    }
    return false
}  // This function will return true if the sum of any two numbers is equal to the third number.  It will return false otherwise.  It first checks if all the input values are integers, then it checks if the sum of any two numbers is equal to the third number.  If it finds a match, it returns true, otherwise it returns false.