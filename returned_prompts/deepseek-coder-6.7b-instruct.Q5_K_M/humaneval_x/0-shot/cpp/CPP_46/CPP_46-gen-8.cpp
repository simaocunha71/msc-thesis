    int fib[n+1];
    fib[0] = 0;
    fib[1] = 0;
    fib[2] = 2;
    fib[3] = 0;
    for(int i=4;i<=n;i++){
        fib[i] = fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4];
    }
    return fib[n];
}

int main(){
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("fib4(%d) = %d\n", n, fib4(n));
    return 0;
}
*/

The program creates an array fib of size n+1. Then, it initializes the first four elements of the array to 0, 0, 2, and 0 respectively. After that, it computes the i-th element of the array as the sum of the (i-1)-th, (i-2)-th, (i-3)-th, and (i-4)-th elements of the array for i from 4 to n. Finally, it returns the n-th element of the array.

This program uses a loop to iterate over the range from 4 to n, so it has a time complexity of O(n). The space complexity is also O(n) because it creates an array of size n+1.

This program can be improved by using only two variables to store the last four computed numbers instead of an array. This would reduce the space complexity to O(1).

Here is the improved version of the program:

```C++
#include<iostream>
using namespace std;

int fib4(int n) {
    int fib[4] = {0, 0, 2, 0};
    if(n < 4) return fib[n];
    int sum;
    for(int i=4;i<=n;i++){
        sum = fib[0] + fib[1] + fib[2] + fib[3];
        fib[0] = fib[1];
        fib[1] = fib[2];
        fib