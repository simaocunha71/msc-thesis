    if(x<n)
        return false;
    while(x % n == 0)
    {
        x /= n;
    }
    return x == 1;
}

int main() {
    int x, n;
    printf("Enter x and n:\n");
    scanf("%d %d", &x, &n);
    if(is_simple_power(x, n))
        printf("true");
    else
        printf("false");
    return 0;
}

// end

*/

