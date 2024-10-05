    int count = 0;
    for(int i = 1; i <= 9; i++){
        if(n == 1){
            if(i == 1) count++;
        }else{
            for(int j = 0; j < i; j++){
                int num = i * pow(10, n-1) + j;
                if(num % 10 == 1 || (n > 1 && num / pow(10, n-1) % 10 == 1))
                    count++;
            }
        }
    }
    return count;
}
int main() {
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("The count of the numbers of %d-digit positive integers that start or end with 1 is %d.\n", n, starts_one_ends(n));
    return 0;
}
