    if(lst.size()<2) return NULL;
    sort(lst.begin(), lst.end());
    for(int i=1; i<lst.size(); i++){
        if(lst[i] != lst[0]) return lst[i];
    }
    return NULL;
}

