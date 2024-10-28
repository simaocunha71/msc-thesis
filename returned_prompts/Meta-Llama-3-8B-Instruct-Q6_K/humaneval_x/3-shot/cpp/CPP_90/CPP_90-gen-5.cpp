    if (lst.size()<2) return -1;
    sort(lst.begin(),lst.end());
    if (lst[1]==lst[0]) return -1;
    return lst[1];
}

// Alternative solution
int next_smallest(vector<int> lst){
    if (lst.size()<2) return -1;
    sort(lst.begin(),lst.end());
    return lst[1];
}