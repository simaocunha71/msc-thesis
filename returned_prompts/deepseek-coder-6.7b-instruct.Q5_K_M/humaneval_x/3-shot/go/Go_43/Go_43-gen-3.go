    for i  := range l  {
        for j  := range l  {
            if i  != j  && l[i]  + l[j]  == 0  {
                return true
             }
         }
     }
    return false
}



