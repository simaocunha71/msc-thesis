    sort(l.begin(), l.end());
    vector<int>::iterator new_end = unique(l.begin(), l.end());
    l.erase(new_end, l.end());
    return l;
}


