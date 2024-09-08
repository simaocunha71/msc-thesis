    vector<int> l2;
    for(int i = 0; i < l.size(); i++){
        if(i % 3 == 0){
            l2.push_back(l[i]);
            sort(l2.begin(), l2.end());
        }
        else{
            l2.push_back(l[i]);
        }
    }
    return l2;
}

B:
    vector<int> l2;
    for(int i = 0; i < l.size(); i++){
        if(i % 3 == 0){
            vector<int> temp;
            temp.push_back(l[i]);
            sort(temp.begin(), temp.end());
            for(int j = 0; j < temp.size(); j++){
                l2.push_back(temp[j]);
            }
        }
        else{
            l2.push_back(l[i]);
        }
    }
    return l2;
}

C:
    vector<int> l2;
    for(int i = 0; i < l.size(); i++){
        if(i % 3 == 0){
            for(int j = i; j < l.size(); j++){
                if(j % 3 == 0){
                    l2.push_back(l[j]);
                    sort(l2.begin(), l2.end());
                }
                else{
                    l2.push_back(l[j]);
                }
            }
        }
        else{
            l2.push_back(l[i]);
        }
    }
    return l2;
}

D:
    vector<int> l2;
    for(int i = 0; i < l.size(); i++){
        if(i % 3 == 0){
            for(int j = i; j < l.size(); j++){
                if(j % 3 == 0){
                    l2.push_back(l[j]);
                }
            }
            sort(l2.begin(), l2.end());
        }
        else{
            l2.push_back(l[i]);
        }
    }
    return l2;
}

E:
    vector<int> l2;
    for(int i = 0; i < l.size(); i++){
        if(i % 3 == 0){
            vector<int> temp;
            temp.push_back(l[i]);
            for(int j = i; j < l.size(); j++){
                if(j % 3 == 0){
                    temp.push_back(l[j]);
                }
            }
            sort(temp.begin(), temp.end());
            for(int j = 0; j < temp.size(); j++){
                l2.push_back(temp[j]);
            }
        }
