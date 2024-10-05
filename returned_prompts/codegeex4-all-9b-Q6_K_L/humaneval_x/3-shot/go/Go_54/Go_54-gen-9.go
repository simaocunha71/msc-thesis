    if len(s0) != len(s1){
        return false
    }

    for i:=0; i<len(s0); i++{
        found := false
        for j:=0; j<len(s1); j++{
            if s0[i] == s1[j]{
                found = true
                break
            }
        }
        if !found{
            return false
        }
    }
    return true
}

