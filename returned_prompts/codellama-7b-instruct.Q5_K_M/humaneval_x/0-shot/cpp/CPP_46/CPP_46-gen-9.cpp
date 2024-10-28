    if(n==0||n==1){
        return 0;
    }
    if(n==2){
        return 2;
    }
    if(n==3){
        return 0;
    }
    int a=fib4(n-1)+fib4(n-2)+fib4(n-3)+fib4(n-4);
    return a;
}
int main(){
    printf("%d\n",fib4(5));
    printf("%d\n",fib4(6));
    printf("%d\n",fib4(7));
    return 0;
}
