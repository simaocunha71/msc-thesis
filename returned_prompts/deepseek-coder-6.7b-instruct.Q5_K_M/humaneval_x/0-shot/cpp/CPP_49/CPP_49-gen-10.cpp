    int r;
    if (n == 0)
        return 1;
    else {
        r = modp(n / 2, p);
        if (n % 2 == 0)
            return (r * r) % p;
        else
            return (((r * r) % p) * 2) % p;
    }
}
int main(){
    int n,p;
    scanf("%d %d",&n,&p);
    printf("%d",modp(n,p));
    return 0;
}

*/

int main(){
    int t;
    scanf("%d",&t);
    while(t--){
        int n,p;
        scanf("%d %d",&n,&p);
        printf("%d\n",modp(n,p));
    }
    return 0;
}



/*
