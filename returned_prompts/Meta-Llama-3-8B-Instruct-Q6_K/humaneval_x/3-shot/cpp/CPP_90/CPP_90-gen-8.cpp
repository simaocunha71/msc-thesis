    if (lst.size() < 2)
        return -1;  // or return None, or return NULL, or whatever makes sense in your language
    
    sort(lst.begin(), lst.end());
    for (int i = 1; i < lst.size(); i++)
        if (lst[i] > lst[0])
            return lst[i];
    
    return -1;  // or return None, or return NULL, or whatever makes sense in your language
}

