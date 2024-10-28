if(a==b+c || b==a+c || c==a+b)
{
if(a==int(a) && b==int(b) && c==int(c))
return true;
else
return false;
}
else
return false;
}
int main()
{
float a,b,c;
printf("Enter first number: ");
scanf("%f",&a);
printf("Enter second number: ");
scanf("%f",&b);
printf("Enter third number: ");
scanf("%f",&c);

if(any_int(a,b,c))
printf("true");
else
printf("false");

return 0;
}
