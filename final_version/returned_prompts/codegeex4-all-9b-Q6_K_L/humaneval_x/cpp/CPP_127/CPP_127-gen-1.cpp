#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int IsPrime(int n)
{
    if (n <= 1) return 0;
    if (n == 2 || n == 3) return 1;
    if (n % 2 == 0 || n % 3 == 0) return 0;
    for (int i = 5; i * i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return 0;
    return 1;
}

char* intersection(int a1, int a2, int b1, int b2)
{
    int inter = 0;
    if ((a1 >= b1 && a1 <= b2) || (a2 >= b1 && a2 <= b2))
        inter = abs(a1 - a2);
    else if ((b1 >= a1 && b1 <= a2) || (b2 >= a1 && b2 <= a2))
        inter = abs(b1 - b2);
    if (IsPrime(inter))
        return "YES";
    return "NO";
}

int main()
{
    printf("%s\n", intersection(1, 2, 2, 3)); // "NO"
    printf("%s\n", intersection(-1, 1, 0, 4)); // "NO"
    printf("%s\n", intersection(-3, -1, -5, 5)); // "YES"
    return 0;
}