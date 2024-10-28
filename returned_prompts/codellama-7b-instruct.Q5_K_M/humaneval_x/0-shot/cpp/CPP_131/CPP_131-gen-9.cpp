    if(n==0){
        return 0;
    }
    if(n%2==0){
        n/=2;
        goto A;
    }
    return n;
}
int main(){
    int x;
    scanf("%d",&x);
    printf("%d",digits(x));
    return 0;
}
