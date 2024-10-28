    if(n==0)
    return 0;
    else if(n==1)
    return 1;
    else
    {
        int count=0;
        count+=9;
        count+=1;
        return count;
    }
}
int main()
{
    int n;
    scanf("%d",&n);
    printf("%d",starts_one_ends(n));
}

*/
Here is a program that returns the count of the numbers of n-digit positive integers that start or end with 1

Explanation:
The program first checks if the input number n is 0 or 1. If it is 0, it returns 0, as there are no 0-digit positive integers. If it is 1, it returns 1, as there is only one 1-digit positive integer, which is 1 itself.

For any other positive integer n, the program initializes a variable called count to 0. It then adds 9 to count, as there are 9 one-digit positive integers (from 2 to 9) that do not start or end with 1. It also adds 1 to count, as there is one 1-digit positive integer (1 itself) that starts or ends with 1. Finally, it returns the value of count, which represents the count of n-digit positive integers that start or end with 1.

Note: The program uses the "using namespace std;" statement, which is generally not recommended in C++ programming. It is better to use the "std::" prefix when referring to standard library objects and functions, as it helps avoid name collisions and makes the code more readable.

Here is an improved version of the program:

#include <iostream>
using namespace std;

int starts_one_ends(int n) {
    if (n == 0)
        return 0;
    else if (n == 1)
        return 1;
    else {
        int count = 0;
        count += 9 * pow(10, n - 1); // Add 9 times the number of (n-1)-digit positive integers
        count += 9 * pow(1