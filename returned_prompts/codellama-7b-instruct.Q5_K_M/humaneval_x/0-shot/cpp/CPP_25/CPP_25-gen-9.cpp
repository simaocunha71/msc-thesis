    if(n==1){
        vector<int> v;
        return v;
    }
    vector<int> v;
    for(int i=2;i<=n;i++){
        if(n%i==0){
            v.push_back(i);
            n=n/i;
            goto A;
        }
    }
    return v;
}
int main(){
    int n;
    scanf("%d",&n);
    vector<int> v=factorize(n);
    for(auto x:v){
        printf("%d ",x);
    }
    return 0;
}
