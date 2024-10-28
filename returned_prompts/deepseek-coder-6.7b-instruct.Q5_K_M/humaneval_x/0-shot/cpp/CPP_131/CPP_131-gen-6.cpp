  string s = to_string(n);
  int result = 1;
  bool isOdd = false;
  for(int i = 0; i < s.length(); i++){
    if((s[i] - '0') % 2 != 0){
      result *= (s[i] - '0');
      isOdd = true;
    }
  }
  return isOdd ? result : 0;
}
*/

#include <stdio.h>
#include <stdlib.h>

int digits(int n){

    int result = 1;
    bool isOdd = false;
    while(n){
        int digit = n % 10;
        n /= 10;
        if(digit % 2 != 0){
            result *= digit;
            isOdd = true;
        }
    }
    return isOdd ? result : 0;
}
int main() {
   printf("%d\n", digits(1));
   printf("%d\n", digits(4));
   printf("%d\n", digits(235));
   return 0;
}

/*
    int main() {
        int num;
        printf("Enter a positive integer: ");
        scanf("%d", &num);
        printf("Product of odd digits: %d\n", digits(num));
        return 0;
    }
*/

//Solution:
//The program reads a number n, calculates the product of the odd digits in the number (if any), and returns the result.
//If there are no odd digits, it returns 0.
//The program uses a while loop to iterate over the digits of the number.
//The remainder of n divided by 10 (n % 10) gives the last digit of n, and integer division by 10 (n /= 10) removes the last digit from n.
//If the last digit is odd, it is multiplied with the current product and the product is updated.
//The variable isOdd is used to check if there are any odd digits in the number. If there are, the updated product