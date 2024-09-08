    if(a+b>c && a+c>b && b+c>a)
        return (sqrt((a+b+c)*(a+b-c)*(c+a-b)*(b+c-a))/4);
    else
        return -1;
}
int main(){
float a,b,c;
scanf("%f %f %f",&a,&b,&c);
printf("%f\n",triangle_area(a,b,c));
return 0;
}
