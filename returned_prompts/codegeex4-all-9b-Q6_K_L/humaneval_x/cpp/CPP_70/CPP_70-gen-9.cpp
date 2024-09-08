    sort(lst.begin(), lst.end());
    vector<int> v;
    int i = 0;
    while(!lst.empty()){
        if(i%2 == 0){
            v.push_back(lst[0]);
            lst.erase(lst.begin());
        }
        else{
            v.push_back(lst[lst.size()-1]);
            lst.erase(lst.end()-1);
        }
        i++;
    }
    return v;
}

B:
    sort(lst.begin(), lst.end());
    vector<int> v;
    int i = 0;
    while(!lst.empty()){
        if(i%2 == 0){
            v.push_back(lst[0]);
            lst.erase(lst.begin());
        }
        else{
            v.push_back(lst[1]);
            lst.erase(lst.begin()+1);
        }
        i++;
    }
    return v;

C:
    sort(lst.begin(), lst.end());
    vector<int> v;
    int i = 0;
    while(!lst.empty()){
        if(i%2 == 0){
            v.push_back(lst[0]);
            lst.erase(lst.begin());
        }
        else{
            v.push_back(lst[lst.size()-1]);
            lst.erase(lst.end());
        }
        i++;
    }
    return v;
D:
    sort(lst.begin(), lst.end());
    vector<int> v;
    int i = 0;
    while(!lst.empty()){
        if(i%2 == 0){
            v.push_back(lst[0]);
            lst.erase(lst.begin());
        }
        else{
            v.push_back(lst[lst.size()-1]);
            lst.erase(lst.end()-1);
        }
        i++;
    }
    return v;
E:
    sort(lst.begin(), lst.end());
    vector<int> v;
    int i = 0;
    while(!lst.empty()){
        if(i%2 == 0){
            v.push_back(lst[0]);
            lst.erase(lst.begin());
        }
        else{
            v.push_back(lst[lst.size()-1]);
            lst.erase(lst.end()-1);
        }
        i++;
    }
    return v;
F:
    sort(lst.begin(), lst.end());
    vector<int> v;
    int i = 0;
    while(!lst.empty()){
        if(i%2 == 0){
            v.push_back(lst[0]);
            lst.erase(lst.begin());
        }
        else{
            v.push_back(lst[lst.size()-2]);
            lst.erase(lst.end()-2);
        }
        i++;
    }
