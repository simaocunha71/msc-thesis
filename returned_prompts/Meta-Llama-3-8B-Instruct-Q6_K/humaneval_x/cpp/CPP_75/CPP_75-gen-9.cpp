    int count = 0;
    int i = 2;
    while(i <= a)
    {
        if(a % i == 0)
        {
            int j = 2;
            while(j <= i/2)
            {
                if(i % j == 0)
                {
                    break;
                }
                j++;
            }
            if(j > i/2)
            {
                count++;
            }
        }
        i++;
    }
    return count == 3;
}

int main()
{
    printf("%d\n",is_multiply_prime(30)); // return true
    printf("%d\n",is_multiply_prime(15)); // return false
    return 0;
}

Solution:
The problem is to find a function that determines whether a given number is the product of three prime numbers. The given number is less than 100.

Here is the solution in C++:
```cpp
#include <iostream>
using namespace std;

bool is_multiply_prime(int a) {
    int count = 0;
    for (int i = 2; i <= a; i++) {
        if (a % i == 0) {
            int j = 2;
            while (j <= i / 2) {
                if (i % j == 0) {
                    break;
                }
                j++;
            }
            if (j > i / 2) {
                count++;
                int k = i;
                while (k <= a) {
                    if (a % k == 0) {
                        int l = 2;
                        while (l <= k / 2) {
                            if (k % l == 0) {
                                break;
                            }
                            l++;
                        }
                        if (l > k / 2) {
                            count++;
                            int m = k;
                            while (m <= a) {
                                if (a % m == 0) {
 int n = 2;
 while (n <= m / 2) {
 if (m % n == 0) {
 break;
 }
 n++;
 }
 if (n > m / 2) {
 count++;
 break;
 }
                                }
                                m++;
                            }
                        }
                    }
                    k++;
                }
            }
        }
    }
    return count == 3;
}

int main() {
    cout << is_multiply_prime(30) << endl; // returns true
    cout << is_multiply_prime(15) << endl;