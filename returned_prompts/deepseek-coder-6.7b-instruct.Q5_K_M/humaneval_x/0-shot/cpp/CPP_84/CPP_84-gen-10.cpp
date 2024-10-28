    int i = 0;
    int sum = 0;
    string result = "";
    while(N != 0){
        sum += N % 10;
        N /= 10;
    }
    while(sum != 0){
        result = to_string(sum % 2) + result;
        sum /= 2;
    }
    return result;
}

int main()
{
    int N;
    printf("Enter a positive integer N: ");
    scanf("%d",&N);
    string result = solve(N);
    printf("The sum of digits in binary is: %s",result.c_str());
    return 0;
}
*/
/*
Output:
Enter a positive integer N: 147
The sum of digits in binary is: 1100
*/
#include<stdio.h>
#include<string>
using namespace std;
string solve(int N){
    int i = 0;
    int sum = 0;
    string result = "";
    while(N != 0){
        sum += N % 10;
        N /= 10;
    }
    while(sum != 0){
        result = to_string(sum % 2) + result;
        sum /= 2;
    }
    return result;
}

int main()
{
    int N;
    printf("Enter a positive integer N: ");
    scanf("%d",&N);
    string result = solve(N);
    printf("The sum of digits in binary is: %s",result.c_str());
    return 0;
}

/*
Output:
Enter a positive integer N: 147
The sum of digits in binary is: 1100
*/

// This program calculates the sum of the digits of a given positive integer N in decimal, and returns the sum in binary.
// It works by first calculating the sum of the digits in the given number. Then, it converts this sum to binary by continuously dividing it by 2 and storing the remainder.
// The remainder is the binary digit from least significant to most significant. The result is then returned