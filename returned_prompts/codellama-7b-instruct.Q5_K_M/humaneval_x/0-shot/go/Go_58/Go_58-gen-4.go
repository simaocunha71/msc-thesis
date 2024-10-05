    for _, e1 := range l1 {
        for _, e2 := range l2 {
            if e1 == e2 {
                goto B
            }
        }
        goto C
    }
    return l1

B:
    return l2

C:
    return nil
}




