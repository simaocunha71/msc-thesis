    if(lst.size() <= 1)
        return true;
    if(lst.size() > 1 && lst[0] > lst[1])
        return false;
    for(int i = 1; i < lst.size(); i++){
        if(lst[i] <= lst[i-1])
            return false;
    }
    return true;
}  // is_sorted


