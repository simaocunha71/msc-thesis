    if(n==1) return 1;
    else return n+sum_to_n(n-1);
}
int main(){
    int n;
    scanf("%d",&n);
    printf("%d\n",sum_to_n(n));
    return 0;
}
