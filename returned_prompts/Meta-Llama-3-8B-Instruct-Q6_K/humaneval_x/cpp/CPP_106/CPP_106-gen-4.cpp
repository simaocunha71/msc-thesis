    vector<int> result(n, 0);
    for(int i = 1; i <= n; i++){
        if(i % 2 == 0) // i is even
            result[i-1] = i * fact(i); // calculate the factorial
        else
            result[i-1] = sum(i); // calculate the sum
    }
    return result;
}

int sum(int n){
    int total = 0;
    for(int i = 1; i <= n; i++)
        total += i;
    return total;
}

int fact(int n){
    int total = 1;
    for(int i = 1; i <= n; i++)
        total *= i;
    return total;
}

int main(){
    int n = 5;
    vector<int> result = f(n);
    for(int i = 0; i < n; i++){
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}

