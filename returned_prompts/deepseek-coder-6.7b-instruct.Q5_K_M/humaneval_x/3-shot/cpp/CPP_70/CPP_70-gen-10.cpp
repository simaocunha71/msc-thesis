    sort(lst.begin(), lst.end());
    for(int i = 0; i < lst.size(); i += 2){
        if(i + 1 < lst.size()){
            swap(lst[i], lst[i + 1]);
        }
    }
    return lst;
}


