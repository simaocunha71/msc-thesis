bool below_threshold(vector<int>l, int t){
    for(int i=0; i<l.size(); i++)
    {
        if(l[i] >= t)
        {
            return false;
        }
    }
    return true;
}

B:
bool below_threshold(vector<int>l, int t){
    return all_of(l.begin(), l.end(), [t](int x) { return x < t; });
}

C:
bool below_threshold(vector<int>l, int t){
    return accumulate(l.begin(), l.end(), 0) < t;
}

D:
bool below_threshold(vector<int>l, int t){
    return l.size() == 0 || *min_element(l.begin(), l.end()) >= t;
}

E:
bool below_threshold(vector<int>l, int t){
    return count_if(l.begin(), l.end(), [t](int x) { return x >= t; }) == 0;
}

F:
bool below_threshold(vector<int>l, int t){
    for(int i : l) {
        if(i >= t) {
            return false;
        }
    }
    return true;
}

G:
bool below_threshold(vector<int>l, int t){
    return none_of(l.begin(), l.end(), [t](int x) { return x >= t; });
}

H:
bool below_threshold(vector<int>l, int t){
    return l.empty() || *max_element(l.begin(), l.end()) < t;
}

I:
bool below_threshold(vector<int>l, int t){
    return all_of(l.begin(), l.end(), [](int x) { return x < t; });
}

J:
bool below_threshold(vector<int>l, int t){
    for(int x : l) {
        if(x >= t) {
            return false;
        }
    }
    return true;
}

K:
bool below_threshold(vector<int>l, int t){
    return all_of(l.begin(), l.end(), [t](int x) { return x <= t; });
}

L:
bool below_threshold(vector<int>l, int t){
    return l.empty() || *max_element(l.begin(), l.end()) <= t;
}

M:
bool below_threshold(vector<int>l, int t){
    return all_of(l.begin(), l.end(), [](int x) { return x <= t; });
}

N:
bool below_threshold(vector<int>l, int t){
    return accumulate(l.begin(), l.end(), 0, [](int x, int y