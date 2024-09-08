    vector<int> l_;
    for(int i = 0; i < l.size(); i++){
        if(i % 3 == 0){
            // sort the elements
            sort(l_.begin() + i, l_.end());
        }
        else {
            l_.push_back(l[i]);
        }
    }
    return l_;
}

