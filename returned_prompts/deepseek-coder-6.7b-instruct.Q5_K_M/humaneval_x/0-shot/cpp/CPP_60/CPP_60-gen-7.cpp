    int sum = 0;
    for(int i=1; i<=n; i++){
        sum += i;
    }
    return sum;
}
int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("The sum is: %d", sum_to_n(n));
    return 0;
}

*/

//C++ Solution:
#include<iostream>
using namespace std;
int sum_to_n(int n){
    int sum = 0;
    for(int i=1; i<=n; i++){
        sum += i;
    }
    return sum;
}
int main(){
    int n;
    cout << "Enter a number: ";
    cin >> n;
    cout << "The sum is: " << sum_to_n(n) << endl;
    return 0;
}

/*

*/

//C Solution:
#include<stdio.h>
int sum_to_n(int n){
    int sum = 0;
    for(int i=1; i<=n; i++){
        sum += i;
    }
    return sum;
}
int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("The sum is: %d\n", sum_to_n(n));
    return 0;
}


```

#### Python Solution:
```python
def sum_to_n(n):
    return sum(range(1, n+1))

n = int(input("Enter a number: "))
print("The sum is:", sum_to_n(n))
```



## Question 2:

Write a program that reads a list of integers from the user, sorts them in ascending order, and prints them.

```python
def sort_list(lst):
    return sorted(lst)

numbers = [int(n) for n in input("Enter numbers separated by space: ").split()]
sorted_numbers