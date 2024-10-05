



    if(n==0){
        return 0;
    }
    if(n==1){
        return 0;
    }
    if(n==2){
        return 1;
    }
    int a = fibfib(n-1);
    int b = fibfib(n-2);
    int c = fibfib(n-3);
    return a+b+c;
}
int main(){
    int a = fibfib(1);
    int b = fibfib(5);
    int c = fibfib(8);
    printf("%d %d %d",a,b,c);
    return 0;
}








