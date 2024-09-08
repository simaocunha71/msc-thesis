    vector<int> l_;
    for(int i = 0; i < l.size(); i++){
        if(i % 3 == 0){
            sort(l_.begin() + i, l_.begin() + i + 1);
        }
        else{
            l_.push_back(l[i]);
        }
    }
    return l_;
}

B:
    vector<int> l_;
    for(int i = 0; i < l.size(); i++){
        if(i % 3 == 0){
            int temp = l[i];
            l_.push_back(temp);
            sort(l_.rbegin(), l_.rend());
        }
        else{
            l_.push_back(l[i]);
        }
    }
    return l_;
}

C:
    vector<int> l_;
    for(int i = 0; i < l.size(); i++){
        if(i % 3 == 0){
            vector<int> temp = {l[i]};
            sort(temp.begin(), temp.end());
            l_.insert(l_.end(), temp.begin(), temp.end());
        }
        else{
            l_.push_back(l[i]);
        }
    }
    return l_;
}

D:
    vector<int> l_;
    for(int i = 0; i < l.size(); i++){
        if(i % 3 == 0){
            vector<int> temp;
            temp.push_back(l[i]);
            sort(temp.begin(), temp.end());
            l_.insert(l_.end(), temp.begin(), temp.end());
        }
        else{
            l_.push_back(l[i]);
        }
    }
    return l_;
}

E:
    vector<int> l_;
    for(int i = 0; i < l.size(); i++){
        if(i % 3 == 0){
            vector<int> temp;
            temp.push_back(l[i]);
            sort(temp.begin(), temp.end());
            l_.insert(l_.end(), temp.begin(), temp.end());
        }
        else{
            l_.push_back(l[i]);
        }
    }
    return l_;
}

F:
    vector<int> l_;
    for(int i = 0; i < l.size(); i++){
        if(i % 3 == 0){
            vector<int> temp;
            temp.push_back(l[i]);
            sort(temp.begin(), temp.end());
            l_.insert(l_.end(), temp.begin(), temp.end());
        }
        else{
            l_.push_back(l[i]);
        }
    }
    return l_;
}

G:
   