    int product=1, digit;
    while(n>0){
        digit=n%10;
        if(digit%2==1){
            product*=digit;
        }
        n/=10;
    }
    if(product==1){
        return 0;
    }
    else{
        return product;
    }
}

int main() {

    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    printf("Product of the odd digits: %d", digits(num));

    return 0;
}
*/

//C++ program to solve the above problem
#include<iostream>
using namespace std;
int digits(int n){
    int product=1, digit;
    while(n>0){
        digit=n%10;
        if(digit%2==1){
            product*=digit;
        }
        n/=10;
    }
    if(product==1){
        return 0;
    }
    else{
        return product;
    }
}
int main() {
    int num;
    cout<<"Enter a number: ";
    cin>>num;
    cout<<"Product of the odd digits: "<<digits(num);
    return 0;
}

//C program to solve the above problem
/*
#include<stdio.h>
int digits(int n){
    int product=1, digit;
    while(n>0){
        digit=n%10;
        if(digit%2==1){
            product*=digit;
        }
        n/=10;
    }
    if(product==1){
        return 0;
    }
    else{
        return product;
    }
}
int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    printf("Product of the odd digits: %d", digits(num));
    return 0;
}
*/
```

## Output

```
