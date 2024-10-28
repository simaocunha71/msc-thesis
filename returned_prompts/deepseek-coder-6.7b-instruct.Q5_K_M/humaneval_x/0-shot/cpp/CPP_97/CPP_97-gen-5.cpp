  int a1=abs(a%10);
  int b1=abs(b%10);
  return a1*b1;
}

int main(){
  int a=148,b=412;
  printf("The product of the unit digits of %d and %d is %d\n",a,b,multiply(a,b));
  a=19;b=28;
  printf("The product of the unit digits of %d and %d is %d\n",a,b,multiply(a,b));
  a=2020;b=1851;
  printf("The product of the unit digits of %d and %d is %d\n",a,b,multiply(a,b));
  a=14;b=-15;
  printf("The product of the unit digits of %d and %d is %d\n",a,b,multiply(a,b));
  return 0;
}
```

