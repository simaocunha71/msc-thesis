    if(n==0){
        return 0;
    }
    return n+sum_to_n(n-1);
}
int main(){
    int n;
    scanf("%d",&n);
    printf("%d",sum_to_n(n));
    return 0;
}
请问这段代码中，sum_to_n函数是递归函数吗？为什么？

