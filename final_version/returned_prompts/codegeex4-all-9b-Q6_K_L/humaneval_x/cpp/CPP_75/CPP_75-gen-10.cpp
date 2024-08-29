#include <stdio.h>
int is_prime(int n)
{
    if (n <= 1)
        return 0;
    for (int i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
            return 0;
    }
    return 1;
}
int main()
{
    int a;
    scanf("%d", &a);
    int count = 0;
    for (int i = 2; i <= a; i++)
    {
        if (is_prime(i))
        {
            if (a % i == 0)
            {
                count++;
                a /= i;
                i--;
            }
        }
    }
    if (count == 3)
        printf("true\n");
    else
        printf("false\n");
    return 0;
}

B:
#include <stdio.h>
bool is_prime(int n)
{
    if (n <= 1)
        return false;
    for (int i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
            return false;
    }
    return true;
}
bool is_multiply_prime(int a)
{
    int count = 0;
    for (int i = 2; i <= a; i++)
    {
        if (is_prime(i))
        {
            if (a % i == 0)
            {
                count++;
                a /= i;
                i--;
            }
        }
    }
    if (count == 3)
        return true;
    else
        return false;
}
int main()
{
    int a;
    scanf("%d", &a);
    if (is_multiply_prime(a))
        printf("true\n");
    else
        printf("false\n");
    return 0;
}

C:
#include <stdio.h>
bool is_prime(int n)
{
    if (n <= 1)
        return false;
    for (int i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
            return false;
    }
    return true;
}
bool is_multiply_prime(int a)
{
    int count = 0;
    for (int i = 2; i <= a; i++)
    {
        if (is_prime(i))
        {
            if (a % i == 0)
            {
                count++;
                a /= i;
                i--;
            }
        }
    }
   