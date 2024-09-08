    int count = 0;
    for(int i = 1; i <= 9; i++){
        if(i == 1)
            count++;
        for(int j = 0; j < n-1; j++){
            int num = i * 10 + j+1;
            if(num % 10 == 1)
                count++;
        }
    }
    return count;
}
int main(){
    int n;
    printf("Enter the number of digits: ");
    scanf("%d", &n);
    printf("The count of numbers of %d-digit positive integers that start or end with 1 is %d.\n", n, starts_one_ends(n));
    return 0;
}
B:
    int count = 0;
    for(int i = 1; i <= 9; i++){
        if(i == 1)
            count++;
        for(int j = 0; j < n-1; j++){
            int num = i * 10 + j+1;
            if(num % 10 == 1)
                count++;
        }
    }
    return count;
}

C:
    int count = 0;
    for(int i = 1; i <= 9; i++){
        if(i == 1)
            count++;
        for(int j = 0; j < n-1; j++){
            int num = i * 10 + j+1;
            if(num % 10 == 1)
                count++;
        }
    }
    return count;

D:
    int count = 0;
    for(int i = 1; i <= 9; i++){
        if(i == 1)
            count++;
        for(int j = 0; j < n-1; j++){
            int num = i * 10 + j+1;
            if(num % 10 == 1)
                count++;
        }
    }
    return count;
}

E:
    int count = 0;
    for(int i = 1; i <= 9; i++){
        if(i == 1)
            count++;
        for(int j = 0; j < n-1; j++){
            int num = i * 10 + j+1;
            if(num % 10 == 1)
                count++;
        }
    }
    return count;

F:
    int count = 0;
    for(int i = 1; i <= 9; i++){
        if(i