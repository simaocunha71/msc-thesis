    return (n >> 1) % p;
}
int main(){
    int t;
    scanf("%d",&t);
    while(t--){
        int n,p;
        scanf("%d %d",&n,&p);
        int res = modp(n,p);
        printf("%d\n",res);
    }
    return 0;
}
