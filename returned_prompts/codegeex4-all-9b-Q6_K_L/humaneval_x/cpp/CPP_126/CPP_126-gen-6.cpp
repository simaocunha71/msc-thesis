bool is_sorted(vector<int> lst){
    bool res = true;
    for(int i = 0; i < lst.size() - 1; i++){
        if(lst[i] > lst[i+1]){
            res = false;
            break;
        }
    }
    return res;
}
B:
bool is_sorted(vector<int> lst){
    return is_sorted_until(lst.begin(), lst.end()) == lst.end();
}
C:
bool is_sorted(vector<int> lst){
    return !adjacent_find(lst.begin(), lst.end(), greater<int>()) && unique(lst.begin(), lst.end()) == lst.end();
}
D:
bool is_sorted(vector<int> lst){
    return lst.empty() || equal(lst.begin(), lst.end()-1, lst.begin()+1);
}
E:
bool is_sorted(vector<int> lst){
    return std::is_sorted(lst.begin(), lst.end());
}
F:
bool is_sorted(vector<int> lst){
    return is_sorted_until(lst.begin(), lst.end()) == lst.end();
}

