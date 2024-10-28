    sort(l.begin(), l.end());

    vector<int> r;
    for(int i = 0; i < l.size(); i++){
        if(i == 0 || l[i] != l[i-1]){
            r.push_back(l[i]);
        }
    }
    return r;
}

int main(){
    vector<int> l = {5, 3, 5, 2, 3, 3, 9, 0, 123};
    vector<int> r = unique(l);
    for(auto i: r){
        printf("%d ", i);
    }
    return 0;
}












*/



















































































































































