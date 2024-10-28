    if(number>remaining){
        number=number-remaining;
        remaining=0;
        goto A;
    }
    else{
        number=number+remaining;
        remaining=0;
        goto A;
    }
    return {number,remaining};
}
int main() {
    int n,m,r;
    while(scanf("%d%d%d",&n,&m,&r)!=EOF){
        vector<int>ans=eat(n,m,r);
        printf("%d %d\n",ans[0],ans[1]);
    }
    return 0;
}



