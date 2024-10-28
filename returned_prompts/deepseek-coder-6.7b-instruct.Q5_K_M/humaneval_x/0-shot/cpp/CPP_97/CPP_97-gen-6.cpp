/*
We get the unit digits by taking the modulo 10 of the numbers.
Then we multiply these values and return the result.
*/
return (abs(a%10) * abs(b%10));
}
int main(){
int a,b;
printf("Enter first number: ");
scanf("%d",&a);
printf("Enter second number: ");
scanf("%d",&b);
printf("Product of unit digits: %d\n",multiply(a,b));
return 0;
}
*/
//M:
