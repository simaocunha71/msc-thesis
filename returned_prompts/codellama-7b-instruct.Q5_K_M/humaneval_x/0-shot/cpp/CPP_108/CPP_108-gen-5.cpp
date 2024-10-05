    int cnt=0;
    for(int i=0;i<n.size();i++){
        int x=n[i];
        if(x<0) x=-x;
        while(x){
            if(x%10>0) cnt++;
            x/=10;
        }
    }
    return cnt;
}
int main(){
    vector<int> n;
    int t;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        printf("%d\n",count_nums(n));
    }
}
