    return vector<int>{n};
}
int main(){
    int n = 70;
    vector<int> v = factorize(n);
    for(int i=0;i<v.size();i++){
        printf("%d ",v[i]);
    }
    return 0;
}
