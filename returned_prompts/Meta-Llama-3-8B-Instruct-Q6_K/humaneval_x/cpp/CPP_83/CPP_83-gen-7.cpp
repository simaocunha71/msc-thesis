    int count = 0;
    for(int i = 1; i <= 9; i++){
        for(int j = 0; j < n - 1; j++){
            for(int k = 0; k < 10; k++){
                if(i == 1 || k == 1){
                    count++;
                }
            }
        }
    }
    return count;
}

int main(){
    int n;
    printf("Enter the number of digits: ");
    scanf("%d", &n);
    printf("Number of n-digit positive integers that start or end with 1: %d", starts_one_ends(n));
    return 0;
}

