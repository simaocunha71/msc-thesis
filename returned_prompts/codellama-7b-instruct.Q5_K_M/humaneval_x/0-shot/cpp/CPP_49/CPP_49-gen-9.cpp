    if(n==1){
        return 1;
    }
    if(n==0){
        return 0;
    }
    if(n==2){
        return 2;
    }
    if(n>p){
        n=n%p;
        goto A;
    }
    return n;
}

B:
int main(){
    int n,p;
    scanf("%d",&n);
    scanf("%d",&p);
    if(n>=p){
        n=n%p;
        goto B;
    }
    printf("%d",modp(n,p));
    return 0;
}

C:
int main(){
    int n,p;
    scanf("%d",&n);
    scanf("%d",&p);
    if(n>=p){
        n=n%p;
        goto C;
    }
    printf("%d",modp(n,p));
    return 0;
}

D:
int main(){
    int n,p;
    scanf("%d",&n);
    scanf("%d",&p);
    if(n>=p){
        n=n%p;
        goto D;
    }
    printf("%d",modp(n,p));
    return 0;
}
E:
int main(){
    int n,p;
    scanf("%d",&n);
    scanf("%d",&p);
    if(n>=p){
        n=n%p;
        goto E;
    }
    printf("%d",modp(n,p));
    return 0;
}
F:
int main(){
    int n,p;
    scanf("%d",&n);
    scanf("%d",&p);
    if(n>=p){
        n=n%p;
        goto F;
    }
    printf("%d",modp(n,p));
    return 0;
}

G:
int main(){
    int n,p;
    scanf("%d",&n);
   