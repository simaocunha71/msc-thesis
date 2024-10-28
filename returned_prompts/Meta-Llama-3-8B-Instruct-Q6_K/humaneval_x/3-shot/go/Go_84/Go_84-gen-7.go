    binary := strconv.FormatInt(int64(N), 2)
    sum := 0
    for _, c := range binary {
        if c == '1' {
            sum += 1
        }
    }
    return strconv.Itoa(sum)
}  // This function works only for positive integers. If you want to include negative integers also, you need to convert the number to positive and then handle the sign separately. Also, the constraint 0 ≤ N ≤ 10000 is not checked in this function. You might want to add some error checking code to make it more robust.