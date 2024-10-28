    sort(l.begin(), l.end());
    vector<int> ret;
    for(int i=0; i<l.size(); i++){
        if(i==0 || l[i]!=l[i-1]){
            ret.push_back(l[i]);
        }
    }
    return ret;
}
int main(){
    vector<int> l = {5, 3, 5, 2, 3, 3, 9, 0, 123};
    vector<int> ret = unique(l);
    for(int i=0; i<ret.size(); i++){
        printf("%d, ", ret[i]);
    }
    return 0;
}
