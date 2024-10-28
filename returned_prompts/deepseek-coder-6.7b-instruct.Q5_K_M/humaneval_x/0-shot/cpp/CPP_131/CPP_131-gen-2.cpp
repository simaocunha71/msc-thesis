    int product = 1;
    int digit;
    while(n){
        digit = n % 10;
        if(digit % 2 != 0){
            product *= digit;
        }
        n /= 10;
    }
    if(product == 1){
        return 0;
    }
    else{
        return product;
    }
}

int main(){
    int n;
    printf("Enter a positive integer: ");
    scanf("%d",&n);
    printf("Product of odd digits is: %d",digits(n));
    return 0;
}
*/


#include<stdio.h>
int digits(int n){
    int product = 1;
    int digit;
    while(n){
        digit = n % 10;
        if(digit % 2 != 0){
            product *= digit;
        }
        n /= 10;
    }
    return product == 1 ? 0 : product;
}
int main(){
    int n;
    printf("Enter a positive integer: ");
    scanf("%d",&n);
    printf("Product of odd digits is: %d",digits(n));
    return 0;
}
//T:O(log(n)), S:O(1)
//This is a straightforward solution where we loop through each digit in the number, check if it's odd, and if it is, multiply it to the product. The time complexity is O(log(n)) because we're iterating through each digit in the number. The space complexity is O(1) because we're using a constant amount of space.
//This solution uses the ternary operator which is a concise way to write an if-else statement. It's equivalent to:
//if(product == 1) return 0; else return product;
//In this case, if the product is equal to 1, it returns 0, otherwise it returns the product.
//The function digits(n) returns the product of the odd digits in n. If all digits are even, it returns 0.
//If n = 1, the function returns 1