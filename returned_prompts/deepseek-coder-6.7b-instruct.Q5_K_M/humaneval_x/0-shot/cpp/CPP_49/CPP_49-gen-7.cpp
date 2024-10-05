    if(n == 0)
        return 1;
    if(n == 1)
        return 2;
    int half_pow = modp(n / 2, p);
    if(n % 2 == 0)
        return (half_pow * half_pow) % p;
    else
        return (2 * ((half_pow * half_pow) % p) % p);
}

int main()
{
    int n, p;
    scanf("%d %d", &n, &p);
    printf("%d\n", modp(n, p));
    return 0;
}
*/

//src/tasks/08_euclidean_algorithm.cpp
/*
