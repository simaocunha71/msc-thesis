    vector<int> l_;
    for(int i = 0; i < l.size(); i++){
        if(i % 3 == 0){
            vector<int> temp(l.begin() + i, l.begin() + i + 1);
            sort(temp.begin(), temp.end());
            l_.push_back(temp[0]);
        }else{
            l_.push_back(l[i]);
        }
    }
    return l_;
}

