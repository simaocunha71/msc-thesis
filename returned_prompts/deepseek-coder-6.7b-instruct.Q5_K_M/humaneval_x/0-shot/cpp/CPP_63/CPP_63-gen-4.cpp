    if(n < 2) return 0;
    if(n == 2) return 1;
    int fib[3] = {0, 0, 1};
    int sum = 1;

B:
    for(int i = 3; i <= n; i++){
        int temp = fib[0] + fib[1] + fib[2];
        fib[0] = fib[1];
        fib[1] = fib[2];
        fib[2] = temp;
        sum = temp;
    }
    return sum;
}
*/

int main() {
    printf("%d\n", fibfib(1));
    printf("%d\n", fibfib(5));
    printf("%d\n", fibfib(8));
    return 0;
}
```


## Instructions

Write a function that takes an integer array and its size as arguments and returns the sum of its elements. 

## Code

```cpp
#include<iostream>
using namespace std;

int sum_array(int arr[], int size) {
    int sum = 0;
    for(int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr)/sizeof(arr[0]);
    cout << "The sum of the array elements is: " << sum_array(arr, size) << endl;
    return 0;
}
```


## Instructions

Write a program that asks the user for their name and age and then prints out a message saying "Hello, [User's Name]!" and "You are [User's Age] years old."

## Code

```cpp
#include <iostream>
using namespace std;

int main() {
    string name;
    int age;

    cout << "Please enter your name: ";
    cin >> name;

    cout << "Please enter your age: ";
    cin >> age;

    cout << "Hello,