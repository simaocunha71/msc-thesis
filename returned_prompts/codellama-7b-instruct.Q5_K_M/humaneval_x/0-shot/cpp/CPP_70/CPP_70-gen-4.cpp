    if(lst.empty()){
        return {};
    }
    vector<int> res;
    sort(lst.begin(), lst.end());
    int min = lst[0];
    int max = lst[lst.size()-1];
    for(int i=1;i<lst.size();i++){
        if(lst[i]>max){
            res.push_back(max);
            max = lst[i];
        }
        else{
            res.push_back(min);
            min = lst[i];
        }
    }
    res.push_back(min);
    res.push_back(max);
    return res;
}

