    vector<int> res;
    vector<int> temp = lst;
    int i = 0, j = 0;
    while(i < temp.size()){
        j = i + 1;
        while(j < temp.size() && temp[i] <= temp[j]){
            j++;
        }
        if(j < temp.size()){
            res.push_back(temp[j]);
            temp.erase(temp.begin() + j);
        }
        else{
            res.push_back(temp[i]);
            temp.erase(temp.begin() + i);
        }
        i++;
    }
    return res;
}

B:
    vector<int> res;
    for(int i = 0; i < lst.size(); i++){
        int min = lst[i];
        for(int j = i; j < lst.size(); j++){
            if(lst[j] < min){
                min = lst[j];
            }
        }
        for(int j = i; j < lst.size(); j++){
            if(lst[j] == min){
                res.push_back(min);
                lst.erase(lst.begin() + j);
                break;
            }
        }
    }
    return res;
}

C:
    vector<int> res;
    for(int i = 0; i < lst.size(); i++){
        int min = lst[i];
        for(int j = i; j < lst.size(); j++){
            if(lst[j] < min){
                min = lst[j];
            }
        }
        for(int j = i; j < lst.size(); j++){
            if(lst[j] == min){
                res.push_back(min);
                lst.erase(lst.begin() + j);
                break;
            }
        }
    }
    return res;
}

D:
    vector<int> res;
    for(int i = 0; i < lst.size(); i++){
        int min = lst[i];
        for(int j = i; j < lst.size(); j++){
            if(lst[j] < min){
                min = lst[j];
            }
        }
        for(int j = i; j < lst.size(); j++){
            if(lst[j] == min){
                res.push_back(min);
                lst.erase(lst.begin() + j);
                break;
            }
        }
    }
    return res;
}
