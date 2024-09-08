    int count = 0;
    for(int i = 0; i < n; i++){
        if(i % 11 == 0 || i % 13 == 0){
            while(i > 0){
                if(i % 10 == 7){
                    count++;
                }
                i /= 10;
            }
        }
    }
    return count;
}

int main(){
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    printf("The number of times the digit 7 appears in integers less than %d which are divisible by 11 or 13 is %d.\n", n, fizz_buzz(n));
    return 0;
}

