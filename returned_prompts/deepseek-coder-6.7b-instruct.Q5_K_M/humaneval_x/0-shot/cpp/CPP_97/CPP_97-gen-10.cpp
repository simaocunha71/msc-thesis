  int x, y;
  x = abs(a%10);
  y = abs(b%10);
  return x*y;
}

int main() {
  int a, b;
  printf("Enter two numbers: ");
  scanf("%d %d", &a, &b);
  printf("Product of unit digits: %d\n", multiply(a, b));
  return 0;
}

Note: In the code, I have used the modulus operator (%) to find the unit digit of the numbers. abs() function is used to get the absolute value of the number as the unit digit of a negative number is not defined.
*/

#include<stdio.h>
#include<math.h>
int multiply(int a,int b){

  int x, y;
  x = abs(a%10);
  y = abs(b%10);
  return x*y;
}

int main() {
  int a, b;
  printf("Enter two numbers: ");
  scanf("%d %d", &a, &b);
  printf("Product of unit digits: %d\n", multiply(a, b));
  return 0;
}

Note: In the code, I have used the modulus operator (%) to find the unit digit of the