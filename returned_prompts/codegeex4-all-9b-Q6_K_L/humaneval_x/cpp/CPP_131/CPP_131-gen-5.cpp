#include <stdio.h>
int main()
{
    int n;
    printf("Enter a positive integer: ");
    scanf("%d", &n);
    int product = 1;
    while (n > 0) {
        int digit = n % 10;
        if (digit % 2 != 0) {
            product *= digit;
        }
        n /= 10;
    }
    printf("Product of odd digits: %d\n", product);
    return 0;
}

B:
#include <stdio.h>
#include <string.h>
int main()
{
    char num[20];
    printf("Enter a positive integer: ");
    scanf("%s", num);
    int product = 1;
    for (int i = 0; i < strlen(num); i++) {
        if (num[i] % 2 != 0) {
            product *= num[i];
        }
    }
    printf("Product of odd digits: %d\n", product);
    return 0;
}

C:
#include <stdio.h>
#include <string.h>
int main()
{
    char num[20];
    printf("Enter a positive integer: ");
    scanf("%s", num);
    int product = 1;
    for (int i = 0; i < strlen(num); i++) {
        if ((num[i] - '0') % 2 != 0) {
            product *= (num[i] - '0');
        }
    }
    printf("Product of odd digits: %d\n", product);
    return 0;
}

D:
#include <stdio.h>
int main()
{
    int n;
    printf("Enter a positive integer: ");
    scanf("%d", &n);
    int product = 1;
    while (n > 0) {
        int digit = n % 10;
        if (digit % 2 != 0) {
            product *= digit;
        }
        n /= 10;
    }
    printf("Product of odd digits: %d\n", product);
    return 0;
}

E:
#include <stdio.h>
int main()
{
    int n;
    printf("Enter a positive integer: ");
    scanf("%d", &n);
    int product = 1;
    while (n > 0) {
        int digit = n % 10;
        if (digit % 2 != 0) {
            product *= digit;
        }
        n = n / 10;
   