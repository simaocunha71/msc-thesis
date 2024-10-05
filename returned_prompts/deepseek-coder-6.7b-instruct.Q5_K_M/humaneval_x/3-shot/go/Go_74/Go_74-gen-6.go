    return func() []string {
        if count1(lst1) < count1(lst2) {
            return lst1
        }
        return lst2
    }()
}


