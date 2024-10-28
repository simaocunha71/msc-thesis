    for _, v := range lst1 {
        if v%2 != 0 {
            for _, w := range lst2 {
                if w%2 == 0 {
                    lst1 = append(lst1[:len(lst1)-1], lst1[len(lst1)-1:]...)
                    lst2 = append(lst2[:len(lst2)-1], w)
                    break
                }
            }
            return "YES"
        }
    }
    return "NO"
}