    vector<int> v;
    for(int i = 0; i < numbers.size(); i++){
        bool found = false;
        for(int j = 0; j < v.size(); j++){
            if(numbers[i] == v[j]){
                found = true;
                break;
            }
        }
        if(!found) v.push_back(numbers[i]);
    }
    return v;
}

B:
    vector<int> v;
    v.reserve(10000);
    for(int i = 0; i < numbers.size(); i++) {
        bool found = false;
        for(int j = 0; j < v.size(); j++) {
            if(numbers[i] == v[j]) {
                found = true;
                break;
            }
        }
        if(!found) v.push_back(numbers[i]);
    }
    return v;
}

C:
    vector<int> v;
    for(int i = 0; i < numbers.size(); i++) {
        bool found = false;
        for(int j = 0; j < v.size(); j++) {
            if(numbers[i] == v[j]) {
                found = true;
                break;
            }
        }
        if(!found) v.push_back(numbers[i]);
    }
    return v;
}

D:
    vector<int> v;
    v.reserve(numbers.size());
    for(int i = 0; i < numbers.size(); i++) {
        bool found = false;
        for(int j = 0; j < v.size(); j++) {
            if(numbers[i] == v[j]) {
                found = true;
                break;
            }
        }
        if(!found) v.push_back(numbers[i]);
    }
    return v;
}

E:
    vector<int> v;
    v.reserve(numbers.size());
   