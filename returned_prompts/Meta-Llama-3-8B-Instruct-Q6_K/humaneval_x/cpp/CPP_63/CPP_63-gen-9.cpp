    if(n <= 1){
        return 0;
    }
    else if(n == 2){
        return 1;
    }
    else{
        int a = 0;
        int b = 0;
        int c = 1;
        for(int i = 3; i <= n; i++){
            int temp = a + b + c;
            a = b;
            b = c;
            c = temp;
        }
        return c;
    }
}
int main(){
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("The %d-th element of the fibfib sequence is: %d\n", n, fibfib(n));
    return 0;
}
