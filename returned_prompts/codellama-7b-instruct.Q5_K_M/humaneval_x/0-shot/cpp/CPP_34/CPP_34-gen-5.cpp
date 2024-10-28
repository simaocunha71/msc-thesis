    vector<int> r(l.size());
    sort(l.begin(), l.end());
    r[0] = l[0];
    for(int i = 1; i < l.size(); i++){
        if(l[i] != l[i-1]){
            r[i] = l[i];
        }
    }
    return r;
}

