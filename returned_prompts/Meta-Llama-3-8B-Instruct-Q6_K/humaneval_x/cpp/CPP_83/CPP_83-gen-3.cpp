    int count = 0;
    for(int i = 1; i <= 9; i++){
        for(int j = 0; j < n; j++){
            if(i == 1 || j == n-1){
                count++;
            }
        }
    }
    return count;
}
int main()
{
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("Number of n-digit positive integers that start or end with 1: %d\n", starts_one_ends(n));
    return 0;
}

