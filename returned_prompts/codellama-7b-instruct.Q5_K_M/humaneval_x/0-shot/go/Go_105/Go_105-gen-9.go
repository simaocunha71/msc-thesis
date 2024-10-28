    for i := 1; i <= 9; i++ {
        for _, value := range arr {
            if value == i {
                continue A
            }
        }
        return []string{}
    }
    return []string{"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}
}

