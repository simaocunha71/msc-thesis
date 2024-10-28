    sort(lst.begin(), lst.end());
    for(size_t i = 0; i < lst.size() / 2; i++){
        swap(lst[i], lst[lst.size() - 1 - i]);
    }
    return lst;
}


