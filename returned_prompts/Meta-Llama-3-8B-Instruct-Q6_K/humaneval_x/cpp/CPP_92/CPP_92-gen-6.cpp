if ((a == floor(a) && b == floor(b) && c == floor(c)) && (a == b + c || a == c + b || a == b + c))
return true;
else
return false;

}
int main()
{
float a,b,c;
scanf("%f%f%f",&a,&b,&c);
if(any_int(a,b,c))
printf("true");
else
printf("false");
return 0;
}