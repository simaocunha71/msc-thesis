    if (lst.size()<2) return -1;
    if (lst[0]>lst[1]) return lst[0];
    return next_smallest(lst.begin()+1,lst.end());
}



