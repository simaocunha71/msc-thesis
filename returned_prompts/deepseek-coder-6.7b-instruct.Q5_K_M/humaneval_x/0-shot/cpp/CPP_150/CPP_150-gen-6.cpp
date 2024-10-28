
    // Your Code Starts Here
    for(int i = 2; i * i <= n; i++)
    {
        if(n % i == 0)
        {
            return y;
        }
    }
    return x;

    // Your Code Ends Here
}

int main() {
    int n, x, y;
    scanf("%d %d %d", &n, &x, &y);
    printf("%d\n", x_or_y(n, x, y));
    return 0;
}

*/

#include <stdio.h>

int is_prime(int n) {
    if(n == 2)
        return 1;
    if(n < 2 || n % 2 == 0)
        return 0;
    for(int i = 3; i * i <= n; i += 2)
        if(n % i == 0)
            return 0;
    return 1;
}

int x_or_y(int n, int x, int y) {
    return is_prime(n) ? x : y;
}

int main() {
    int n, x, y;
    scanf("%d %d %d", &n, &x, &y);
    printf("%d\n", x_or_y(n, x, y));
    return 0;
}


/*
