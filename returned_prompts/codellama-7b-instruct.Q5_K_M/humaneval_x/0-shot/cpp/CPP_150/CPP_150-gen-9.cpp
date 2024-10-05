    if(n==1||n==0)
        return y;

    for(int i=2;i<n;i++){
        if(n%i==0)
            goto B;
    }

    return x;

B:
    return y;
}
int main(){
    int n,x,y;
    scanf("%d", &n);
    scanf("%d", &x);
    scanf("%d", &y);
    printf("%d\n", x_or_y(n,x,y));
    return 0;
}
