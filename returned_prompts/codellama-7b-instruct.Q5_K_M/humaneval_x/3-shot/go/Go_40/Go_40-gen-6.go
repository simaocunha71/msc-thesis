    for i, x := range l{
        for j, y := range l{
            for k, z := range l{
                if i!=j && j!=k && k!=i{
                    if x+y+z == 0{
                        return true
                    }
                }
            }
        }
    }
    return false
}



