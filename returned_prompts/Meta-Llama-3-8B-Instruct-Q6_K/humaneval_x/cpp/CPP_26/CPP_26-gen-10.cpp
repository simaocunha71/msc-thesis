    vector<int> res;
    for(int i = 0; i < numbers.size(); i++){
        bool found = false;
        for(int j = 0; j < res.size(); j++){
            if(numbers[i] == res[j]){
                found = true;
                break;
            }
        }
        if(!found){
            res.push_back(numbers[i]);
        }
    }
    return res;
}

B:
    vector<int> res;
    for(int i = 0; i < numbers.size(); i++){
        bool found = false;
        for(int j = 0; j < res.size(); j++){
            if(numbers[i] == res[j]){
                found = true;
                break;
            }
        }
        if(!found){
            res.push_back(numbers[i]);
        }
    }
    return res;
}

C:
    set<int> s;
    for(int i = 0; i < numbers.size(); i++){
        s.insert(numbers[i]);
    }
    vector<int> res;
    for(set<int>::iterator it = s.begin(); it != s.end(); ++it){
        res.push_back(*it);
    }
    return res;
}

D:
    set<int> s;
    for(int i = 0; i < numbers.size(); i++){
        s.insert(numbers[i]);
    }
    vector<int> res;
    for(set<int>::iterator it = s.begin(); it != s.end(); ++it){
        res.push_back(*it);
    }
    return res;
}

E:
    set<int> s;
    for(int i = 0; i < numbers.size(); i++){
        s.insert(numbers[i]);
    }
    vector<int> res;
    for(set<int>::iterator it = s.begin(); it != s.end(); ++it){
        res.push_back(*it);
    }
    return res;
}

F:
    set<int> s;
    for(int i = 0; i < numbers.size(); i++){
        s.insert(numbers[i]);
    }
    vector<int> res;
    for(set<int>::iterator it = s.begin(); it != s.end(); ++it){
        res.push_back(*it);
    }
    return res;
}

G:
    set<int> s;
    for(int i = 0; i < numbers.size(); i++){
        s.insert(numbers[i]);
    }
    vector<int> res;
    for(set<int>::iterator it = s.begin(); it != s.end(); ++it){
        res.push_back(*it