  int unitDigitA, unitDigitB;
  unitDigitA = abs(a%10);
  unitDigitB = abs(b%10);
  return unitDigitA * unitDigitB;
}

int main(){
  int a = 148, b = 412;
  printf("Product of unit digits: %d\n",multiply(a,b));
  a = 19; b = 28;
  printf("Product of unit digits: %d\n",multiply(a,b));
  a = 2020; b = 1851;
  printf("Product of unit digits: %d\n",multiply(a,b));
  a = 14; b = -15;
  printf("Product of unit digits: %d\n",multiply(a,b));
  return 0;
}
```

This program will output:
```
Product of unit digits: 16
Product of unit digits: 72
Product of unit digits: 0
Product of unit digits: 20
```
*/

int main() {
    printf("%d\n", multiply(148, 412));  // 16
    printf("%d\n", multiply(19, 28));  // 72
    printf("%d\n", multiply(2020, 1851));  // 0
    printf("%d\n", multiply(14, -15));  // 20
    return 0;
}
```

This program will output:
```
16
72
0
20
```


This program works by taking the absolute value of the remainder of the division of the input numbers by 10 (which gives the unit digit). It then multiplies these unit digits together and returns the result.

This program is written in C++, and it uses the standard library, so you don't need to include any additional libraries.































