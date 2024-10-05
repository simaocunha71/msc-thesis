    int odd_product = 1;
    int even_flag = 0;
    while(n>0){
        int digit = n%10;
        if(digit%2 != 0){
            odd_product *= digit;
            even_flag = 1;
        }
        n /= 10;
    }
    return even_flag == 1 ? odd_product : 0;
}

int main(){
    int n;
    printf("Enter a number:");
    scanf("%d",&n);
    printf("%d",digits(n));
    return 0;
}
*/

*/

#include<stdio.h>
#include<string>
using namespace std;
int digits(int n){
    int odd_product = 1;
    int even_flag = 0;
    while(n>0){
        int digit = n%10;
        if(digit%2 != 0){
            odd_product *= digit;
            even_flag = 1;
        }
        n /= 10;
    }
    return even_flag == 1 ? odd_product : 0;
}

int main(){
    int n;
    printf("Enter a number:");
    scanf("%d",&n);
    printf("%d",digits(n));
    return 0;
}

// Write a C++ program that takes an integer n as input and prints the sum of the digits of n.
// For example, if the input is 123, the output should be 6 (1+2+3).

/*
#include<stdio.h>
int main(){
    int n,sum=0;
    printf("Enter a number:");
    scanf("%d",&n);
    while(n>0){
        sum += n%10;
        n /= 10;
    }
    printf("Sum of digits: %d",sum);
    return 0;
}
*/

// Write a C++ program that takes an integer n as input and prints the product of the digits of n.
// For example, if the input is 123,