    for i := n / 2; i > 0; i-- {
        if n%i == 0 {
            return i
        }
    }
    return 1
}  // This is more efficient as it starts from half of n.