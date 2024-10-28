    vector<int> res;
    sort(lst.begin(), lst.end());
    int min = lst[0];
    int max = lst[lst.size()-1];
    int mid = 0;
    for(int i=0; i<lst.size(); i++){
        if(lst[i]==min){
            min = mid;
            mid = max;
            max = lst[i];
        }
        res.push_back(max);
        lst.erase(lst.begin()+i);
    }
    return res;
}

