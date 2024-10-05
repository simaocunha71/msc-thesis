    vector<int> v;
    if(n==0){
        v.push_back(1);
        return v;
    }
    if(n==1){
        v.push_back(1);
        return v;
    }
    if(n%2==0){
        v.push_back(1);
        for(int i=2;i<=n;i++){
            if(i%2==0){
                int res=1;
                for(int j=i;j>=2;j--){
                    res*=j;
                }
                v.push_back(res);
            }else{
                int sum=0;
                for(int j=1;j<=i;j++){
                    sum+=j;
                }
                v.push_back(sum);
            }
        }
    }else{
        v.push_back(1);
        for(int i=2;i<=n;i++){
            if(i%2==1){
                int sum=0;
                for(int j=1;j<=i;j++){
                    sum+=j;
                }
                v.push_back(sum);
            }else{
                int res=1;
                for(int j=i;j>=2;j--){
                    res*=j;
                }
                v.push_back(res);
            }
        }
    }
    return v;
}

int main(){
    int n;
    scanf("%d",&n);
    vector<int> v=f(n);
    for(int i=0;i<n;i++)
        printf("%d ",v[i]);
    printf("\n");
    return 0;
}












































































