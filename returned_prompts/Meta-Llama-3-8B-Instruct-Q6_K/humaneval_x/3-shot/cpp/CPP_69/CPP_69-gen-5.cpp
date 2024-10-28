    int max = -1, count = 0;
    for (int i = 0; i < lst.size(); i++) {
        int temp = lst[i];
        if (temp > max && count >= temp) {
            max = temp;
        }
        int cnt = 0;
        for (int j = 0; j < lst.size(); j++) {
            if (lst[j] == temp) {
                cnt++;
            }
        }
        if (cnt >= temp && temp > max) {
            max = temp;
        }
    }
    return max;
} // end function search
// or
int search(vector<int> lst){
    map<int, int> m;
    for(int i = 0; i < lst.size(); i++){
        m[lst[i]]++;
    }
    int max = 0;
    for(auto it = m.begin(); it != m.end(); it++){
        if(it->second >= it->first && it->first > max){
            max = it->first;
        }
    }
    return max > 0 ? max : -1;
} // end function search
// or
int search(vector<int> lst){
    unordered_map<int, int> m;
    for(int i = 0; i < lst.size(); i++){
        m[lst[i]]++;
    }
    int max = 0;
    for(auto it = m.begin(); it != m.end(); it++){
        if(it->second >= it->first && it->first > max){
            max = it->first;
        }
    }
    return max > 0 ? max : -1;
} // end function search
// or
int search(vector<int> lst){
    map<int, int> m;
    for(int i = 0; i < lst.size(); i++){
        m[lst[i]]++;
    }
    int max = 0;
    for(auto it = m.begin(); it != m.end(); it++){
        if(it->second >= it->first){
            max = max > it->first ? max : it->first;
        }
    }
    return max > 0 ? max : -1;
} // end function search
// or
int search(vector<int> lst){
    map<int, int> m;
    for(int i = 0; i < lst.size(); i++){
        m[lst[i]]++;
    }
    int max = 0;
    for(auto it = m