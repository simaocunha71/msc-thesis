    int sum = 0;
    for(int i = 1; i <= n; i++){
        sum += i;
    }
    return sum;
}
int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Sum from 1 to %d is: %d\n", n, sum_to_n(n));
    return 0;
}

S:
Here is a simple C++ program that calculates the sum of all numbers from 1 to n using a for loop. The function `sum_to_n(int n)` calculates the sum and returns it. The main function prompts the user to enter a number, calculates the sum using the function, and then prints the result.

```cpp
#include<stdio.h>
using namespace std;
int sum_to_n(int n){
    int sum = 0;
    for(int i = 1; i <= n; i++){
        sum += i;
    }
    return sum;
}
int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Sum from 1 to %d is: %d\n", n, sum_to_n(n));
    return 0;
}
```
When you run this program, it will ask you to enter a number. After you enter a number, it will calculate the sum of all numbers from 1 to the number you entered and print the result. For example, if you enter 5, it will print "Sum from 1 to 5 is: 15". If you enter 10, it will print "Sum from 1 to 10 is: 55". And so on.