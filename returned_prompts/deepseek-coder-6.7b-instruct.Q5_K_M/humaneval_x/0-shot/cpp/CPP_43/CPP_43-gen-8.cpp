    unordered_set<int> s;
    for(int i=0;i<l.size();i++){
        if(s.find(-l[i]) != s.end()){
            return true;
        }
        s.insert(l[i]);
    }
    return false;
}

int main(){
    vector<int> v1 {1, 3, 5, 0};
    vector<int> v2 {1, 3, -2, 1};
    vector<int> v3 {1, 2, 3, 7};
    vector<int> v4 {2, 4, -5, 3, 5, 7};