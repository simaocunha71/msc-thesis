    if(p==1)
        return n%2==0?1:0;
    if(n<1)
        return 1;
    if(n%2==0)
        return modp(n/2,p)%p;
    else
        return (modp(n-1,p)%p)*2%p;

B:
    int res = 1;
    int n1 = n;
    while(n1 > 0)
    {
        if(n1 % 2 == 1)
            res = (res * 2) % p;
        n1 = n1 / 2;
    }
    return res;
}
int main() {
    printf("%d\n",modp(3,5));
    printf("%d\n",modp(1101,101));
    printf("%d\n",modp(0,101));
    printf("%d\n",modp(3,11));
    printf("%d\n",modp(100,101));
    return 0;
}
C:
    int modp(int n,int p){
    int res = 1;
    while(n > 0)
    {
        if(n % 2 == 1)
            res = (res * 2) % p;
        n = n / 2;
    }
    return res;
}
int main() {
    printf("%d\n",modp(3,5));
    printf("%d\n",modp(1101,101));
    printf("%d\n",modp(0,101));
    printf("%d\n",modp(3,11));
    printf("%d\n",modp(100,101));
    return 0;
}
D:
    int modp(int n,int p){
    if(p==1)
        return 0;
    if(n<1)
        return 1;
    if(n%2==0)
        return modp(n/2,p);
    else
        return (modp(n-1,p)%p)*2%p;
}
int main() {
    printf("%d\n",modp(3,5));
    printf("%d\n",modp(1101,101));
    printf("%d\n",modp(0,101));
    printf("%d\n",modp(3,11));
    printf("%d\n",modp(100,101));
    return 0;
}
E:
    int modp(int n,int p){
    if(p==1)
        return