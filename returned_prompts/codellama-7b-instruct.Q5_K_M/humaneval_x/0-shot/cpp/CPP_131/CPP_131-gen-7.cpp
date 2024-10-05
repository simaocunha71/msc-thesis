    if(n==0) return 0;
    if(n%2==0) {n/=2; goto A;}
    else {n--; goto A;}
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d", digits(n));
}

