    vector<float> l_;
    for(int i=0; i<l.size(); i++){
        if(i%2==0){
            vector<float> temp;
            for(int j=0; j<l.size(); j++){
                if(j%2==0){
                    temp.push_back(l[j]);
                }
            }
            sort(temp.begin(), temp.end());
            l_.push_back(temp[0]);
        }
        else{
            l_.push_back(l[i]);
        }
    }
    return l_;
}

