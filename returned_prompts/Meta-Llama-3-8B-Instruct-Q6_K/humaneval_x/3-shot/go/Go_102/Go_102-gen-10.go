    if x%2==0 {
        return y
    }else if y%2==0 {
        return y
    }else if x%2!=0 && y%2!=0 {
        return -1
    }else if x%2==0 && y%2!=0 {
        for i := x; i <= y; i++ {
            if i % 2 == 0 {
                return i
            }
        }
        return -1
    }else if x%2!=0 && y%2==0 {
        for i := x; i <= y; i++ {
            if i % 2 == 0 {
                return i
            }
        }
        return -1
    }
}