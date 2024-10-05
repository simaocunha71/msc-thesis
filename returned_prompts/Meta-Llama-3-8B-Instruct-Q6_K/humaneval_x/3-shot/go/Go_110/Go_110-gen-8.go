    for _, num := range lst1 {
        if num % 2 != 0 {
            for _, num2 := range lst2 {
                if num2 % 2 == 0 {
                    lst1 = append(lst1[:i], lst1[i+1:]...)
                    lst2 = append(lst2[:j], append([]int{num}, lst2[j+1:]...)...)
                    return "YES"
                }
            }
        }
    }
    return "NO"
}