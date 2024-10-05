    int i = 2;
B:
    if (n % i == 0){
        n = n / i;
        if (n == 1)
            return i;
        else
            goto B;
    }
    else{
        i = i + 1;
        goto A;
    }
}
int main(){
    printf("%d\n", largest_prime_factor(13195));
    printf("%d\n", largest_prime_factor(2048));
    return 0;
}

*/

#include<iostream>
using namespace std;
int largest_prime_factor(int n){
    int i = 2;
    while(1){
        if (n % i == 0){
            n = n / i;
            if (n == 1)
                return i;
        }
        else{
            i = i + 1;
        }
    }
}
int main(){
    cout << largest_prime_factor(13195) << endl;
    cout << largest_prime_factor(2048) << endl;
    return 0;
}

// This program uses a while loop to continually divide the number by its smallest divisor (i) and update i if the current i does not evenly divide the number. The loop will eventually terminate when n has been completely divided down to its smallest prime factor.

// The program then prints out the largest prime factor of the number 13195 and 2048 using the function largest_prime_factor.

// The largest prime factor of 13195 is 29 and the largest prime factor of 2048 is 2.

// The program utilizes a simple loop structure and no additional data structures. It uses a while loop to repeatedly divide the number by an increasing divisor until the number itself becomes a prime. This prime number is the largest prime factor of the original number.

// The program also utilizes no external libraries or functions. It is written in standard C++ and does not use any advanced concepts or libraries.

// Finally, the program uses a while loop to repeatedly divide the number by an increasing divisor until the number itself becomes a prime. This prime