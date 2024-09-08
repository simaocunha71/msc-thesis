    double log_val=log(x)/log(n);
    if(log_val==int(log_val))
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
    printf("%d\n",is_simple_power(1,4));
    printf("%d\n",is_simple_power(2,2));
    printf("%d\n",is_simple_power(8,2));
    printf("%d\n",is_simple_power(3,2));
    printf("%d\n",is_simple_power(3,1));
    printf("%d\n",is_simple_power(5,3));
    return 0;
}

C:
#include <stdio.h>
#include <math.h>
bool is_simple_power(int x, int n) {
    double log_val = log(x) / log(n);
    if (log_val == round(log_val)) {
        return true;
    } else {
        return false;
    }
}

int main() {
    printf("%d\n", is_simple_power(1, 4));
    printf("%d\n", is_simple_power(2, 2));
    printf("%d\n", is_simple_power(8, 2));
    printf("%d\n", is_simple_power(3, 2));
    printf("%d\n", is_simple_power(3, 1));
    printf("%d\n", is_simple_power(5, 3));
    return 0;
}

B:
#include <stdio.h>
#include <math.h>
bool is_simple_power(int x, int n) {
    double log_val = log(x) / log(n);
    return round(log_val) == log_val;
}

int main() {
    printf("%d\n", is_simple_power(1, 4));
    printf("%d\n", is_simple_power(2, 2));
    printf("%d\n", is_simple_power(8, 2));
    printf("%d\n", is_simple_power(3, 2));
    printf("%d\n", is_simple_power(3, 1));
    printf("%d\n", is_simple_power(5, 3));
    return 0;
}

Explanation:
The function is_simple_power() takes two integer parameters x and n. It checks whether x is a simple power of n or not.
The function uses the log() function to calculate the logarithm of x with base n. It then checks whether the logarithm is an integer or not by comparing it with the rounded value of the logarithm. If