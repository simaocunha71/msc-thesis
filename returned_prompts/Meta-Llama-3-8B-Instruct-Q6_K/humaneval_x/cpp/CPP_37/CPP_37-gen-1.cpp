    vector<float> l_;
    for(int i = 0; i < l.size(); i++){
        if(i % 2 == 0){
            sort(l.begin()+i, l.begin()+i+1);
            l_.push_back(l[i]);
        }
        else{
            l_.push_back(l[i]);
        }
    }
    return l_;
}

