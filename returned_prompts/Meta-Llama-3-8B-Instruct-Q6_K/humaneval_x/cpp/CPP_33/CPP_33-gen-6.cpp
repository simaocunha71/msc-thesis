    vector<int> l_;
    for(int i = 0; i < l.size(); i++){
        if(i % 3 == 0){
            vector<int> temp;
            for(int j = i; j < l.size(); j++){
                if(j % 3 == 0){
                    temp.push_back(l[j]);
                }
            }
            sort(temp.begin(), temp.end());
            for(int k = 0; k < temp.size(); k++){
                l_[push_back(temp[k]);
            }
            i += temp.size() - 1;
        } else {
            l_.push_back(l[i]);
        }
    }
    return l_;
}

