    if(n <= 0){
        return 1;
    }

    return n * special_factorial(n-1);
}

int main() {
    int n = 5;
    printf("%lld\n", special_factorial(n));
    return 0;
}

