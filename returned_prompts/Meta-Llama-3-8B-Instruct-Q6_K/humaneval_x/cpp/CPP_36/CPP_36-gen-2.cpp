    int count = 0;
    for(int i = 1; i < n; i++){
        if(i % 11 == 0 || i % 13 == 0){
            while(i > 0){
                if(i % 10 == 7){
                    count++;
                    i /= 10;
                }
                else
                    i /= 10;
            }
        }
    }
    return count;
}

int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("The number of times 7 appears in integers less than %d which are divisible by 11 or 13 is: %d\n", n, fizz_buzz(n));
    return 0;
}