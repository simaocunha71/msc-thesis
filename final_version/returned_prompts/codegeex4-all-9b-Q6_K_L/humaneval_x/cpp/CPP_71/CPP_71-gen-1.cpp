float s;
s=(a+b+c)/2;
float area;
area=sqrt(s*(s-a)*(s-b)*(s-c));
return area;
}
int main(){
float a,b,c;
float area;
printf("Enter the value of a:");
scanf("%f",&a);
printf("Enter the value of b:");
scanf("%f",&b);
printf("Enter the value of c:");
scanf("%f",&c);
if((a+b>c)&&(a+c>b)&&(b+c>a)){
area=triangle_area(a,b,c);
printf("The area of triangle is:%.2f",area);
}
else{
printf("Invalid triangle");
}
return 0;
}<|code_prefix|>
