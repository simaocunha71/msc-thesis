    for _, num := range lst1 {
        if num%2 != 0 {
            for _, num2 := range lst2 {
                if num2%2 == 0 {
                    lst1 = append([]int{}, lst1...)
                    lst1 = append(lst1, num2)
                    lst2 = append([]int{}, lst2...)
                    lst2 = append(lst2, num)
                    return "YES"
                }
            }
            return "NO"
        }
    }
    return "YES"
}