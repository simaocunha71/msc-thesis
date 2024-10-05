    if(n==1 || n==0)
        return false;

    for(int i=2;i*i<=n;i++){
        if(n%i==0)
            return false;
    }
    return true;
}

int main(){
    int t;
    long long n;
    scanf("%d",&t);
    while(t--){
        scanf("%lld",&n);
        bool a = is_prime(n);
        if(a==true)
            printf("true\n");
        else
            printf("false\n");
    }
    return 0;
}

/*

4
1
2
3
4

*/
