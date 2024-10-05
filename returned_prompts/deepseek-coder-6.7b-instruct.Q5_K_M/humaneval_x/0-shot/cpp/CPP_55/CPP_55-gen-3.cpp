    if (n <= 1)
        return n;
    else
        return fib(n-1) + fib(n-2);
}

int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("%dth Fibonacci number is: %d\n", n, fib(n));
    return 0;
}
```

This program uses the concept of recursion to calculate the Fibonacci sequence.

## Problem 2
Write a C++ program to implement the bubble sort algorithm.

```cpp
#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n) {
    int i, j;
    for (i = 0; i < n-1; i++) {
        for (j = 00; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                // Swap arr[j] and arr[j+1]
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

void printArray(int arr[], int size) {
    int i;
    for (i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr)/sizeof(arr[0]);
    bubbleSort(arr, n);
    cout<<"Sorted array: \n";
    printArray(arr, n);
    return 0;
}
```

This program uses the bubble sort algorithm to sort an array in ascending order. It repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

## Problem 3
Write a C++ program to implement the merge sort algorithm.