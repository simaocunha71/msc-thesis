    for (int i = 2; i < n; i++){
        if (n % i == 0){
            return i;
        }
    }
    return n;
}

int main(int argc, char const *argv[])
{
    int n = 15;
    printf("%d", largest_divisor(n));
    return 0;
}
