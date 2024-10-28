    int n1, n2, i;
    n1 = n2 = 0;
    for(i = 1; i <= n; i++){
        n1++;
        if(n1 == n2){
            goto B;
        }
    }
    return n2;
B:
    for(i = 1; i <= n; i++){
        n2++;
        if(n1 == n2){
            goto A;
        }
    }
    return n1;
}
int main(void){
    int n;
    int c;
    while(scanf("%d", &n) == 1){
        c = car_race_collision(n);
        printf("%d\n", c);
    }
    return 0;
}
