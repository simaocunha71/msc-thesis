    int count=0;
    for(int i=1;i<=9;i++){
        for(int j=0;j<n-1;j++){
            int num=i*pow(10,j)*10+i;
            if(num>=10&&num<=999999){
                count++;
            }
        }
    }
    return count;
}

int main()
{
    int n;
    printf("Enter the number of digits:");
    scanf("%d",&n);
    printf("The count of the numbers of %d-digit positive integers that start or end with 1 is: %d\n",n,starts_one_ends(n));
    return 0;
}
B:
    int count = 0;
    for(int i = 1; i <= 9; i++) {
        if (n == 1) {
            count += 2;
        } else {
            for(int j = 0; j < (int)pow(10, n - 1); j++) {
                int num = i * pow(10, n - 1) + j;
                if (num % 10 == 1 || num / pow(10, n - 1) % 10 == 1) {
                    count++;
                }
            }
        }
    }
    return count;
}

int main() {
    int n;
    printf("Enter the number of digits:");
    scanf("%d", &n);
    printf("The count of the numbers of %d-digit positive integers that start or end with 1 is: %d\n", n, B);
    return 0;
}
C:
    int count = 0;
    if (n == 1) {
        count = 2;
    } else {
        for(int i = 1; i <= 9; i++) {
            for(int j = 0; j < (int)pow(10, n - 1); j++) {
                int num = i * pow(10, n - 1) + j;
                if (num % 10 == 1 || num / pow(10, n - 1) % 10 == 1) {
                    count++;
                }
            }
        }
    }
    return count;
}

int main() {
    int n;
    printf("Enter the number of digits:");
    scanf("%d", &n);
    printf("The count of the numbers of %d-digit positive integers that start or end with 1 is: %d\n", n,