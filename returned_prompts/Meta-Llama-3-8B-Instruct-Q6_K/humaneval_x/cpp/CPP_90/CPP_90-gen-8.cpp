    if(lst.empty()) return NULL;
    vector<int> copy = lst;
    sort(copy.begin(), copy.end());
    for(int i = 1; i < copy.size(); i++){
        if(copy[i] > lst[0]){
            return copy[i];
        }
    }
    return NULL;
}

