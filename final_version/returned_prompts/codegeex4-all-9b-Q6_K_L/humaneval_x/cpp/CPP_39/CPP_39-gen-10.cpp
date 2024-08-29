    int num1=0;
    int num2=1;
    int sum;
    int count=0;
    while(count<n){
        sum=num1+num2;
        num1=num2;
        num2=sum;
        if(is_prime(sum)){
            count++;
        }
    }
    return sum;
}
bool is_prime(int num){
    int count=2;
    while(num%count!=0){
        count++;
    }
    if(count==num){
        return true;
    }
    else{
        return false;
    }
}
int main(){
    int n;
    printf("Enter the value of n: ");
    scanf("%d",&n);
    printf("%d-th prime number in Fibonacci series is: %d\n",n,prime_fib(n));
    return 0;
}

