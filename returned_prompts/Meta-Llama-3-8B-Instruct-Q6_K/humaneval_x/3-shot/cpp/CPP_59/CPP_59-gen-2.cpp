    int i;
    for (i=n/2;i>1;i--)
    {
        if (n%i==0)
        {
            while (n%i==0)
            {
                n=n/i;
            }
        }
    }
    return n;
}  // not efficient for large numbers
// more efficient solution:
#include<math.h>
int largest_prime_factor(int n){
    int i;
    for (i=sqrt(n);i>1;i--)
    {
        if (n%i==0)
        {
            while (n%i==0)
            {
                n=n/i;
            }
        }
    }
    return n;
}  // much faster for large numbers


