    sort(l.begin(),l.end());
    auto it = unique(l.begin(),l.end());
    l.erase(it, l.end());
    return l;
}
int main(){
    vector<int> l = {5, 3, 5, 2, 3, 3, 9, 0, 123};
    vector<int> l2 = unique(l);
    for(int i:l2){
        printf("%d ",i);
    }
    return 0;
}
