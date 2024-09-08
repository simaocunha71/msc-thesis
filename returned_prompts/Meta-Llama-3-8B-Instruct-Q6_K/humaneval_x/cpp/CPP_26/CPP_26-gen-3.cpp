    vector<int> result;
    for(int i = 0; i < numbers.size(); i++){
        bool is_duplicate = false;
        for(int j = 0; j < result.size(); j++){
            if(numbers[i] == result[j]){
                is_duplicate = true;
                break;
            }
        }
        if(!is_duplicate){
            result.push_back(numbers[i]);
        }
    }
    return result;
}

B:
    vector<int> result;
    for(int i = 0; i < numbers.size(); i++){
        if(find(result.begin(), result.end(), numbers[i]) == result.end()){
            result.push_back(numbers[i]);
        }
    }
    return result;
}

C:
    set<int> s;
    for(int num : numbers){
        s.insert(num);
    }
    vector<int> result(s.begin(), s.end());
    return result;

D:
    unordered_map<int, bool> mp;
    vector<int> result;
    for(int num : numbers){
        if(!mp[num]){
            mp[num] = true;
            result.push_back(num);
        }
    }
    return result;
}

E:
    unordered_set<int> s;
    vector<int> result;
    for(int num : numbers){
        if(s.find(num) == s.end()){
            s.insert(num);
            result.push_back(num);
        }
    }
    return result;
}

F:
    sort(numbers.begin(), numbers.end());
    vector<int> result;
    for(int i = 0; i < numbers.size(); i++){
        if(i == 0 || numbers[i] != numbers[i-1]){
            result.push_back(numbers[i]);
        }
    }
    return result;

G:
    unordered_map<int, int> mp;
    vector<int> result;
    for(int num : numbers){
        mp[num]++;
    }
    for(int num : numbers){
        if(mp[num] == 1){
            result.push_back(num);
        }
    }
    return result;
}

H:
    unordered_map<int, int> mp;
    vector<int> result;
    for(int num : numbers){
        if(mp.find(num) == mp.end()){
            mp[num] = 1;
            result.push_back(num);
        }
    }
    return result;
}

I:
    unordered_set<int> s;
    vector<int> result;
    for(int num : numbers){
        if(s.find(num) == s.end()){
            s.insert(num);
            result.push_back(num);
        }
    }
    return