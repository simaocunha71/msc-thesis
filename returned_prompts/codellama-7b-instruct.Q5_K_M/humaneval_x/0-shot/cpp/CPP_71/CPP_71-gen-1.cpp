float area=0;
if(a+b>c){
    area=(a*b)/2;
    return area;
}
else{
    return -1;
}
}
int main()
{
    float a,b,c;
    scanf("%f%f%f",&a,&b,&c);
    printf("%f",triangle_area(a,b,c));
    return 0;
}

Ans:
#include<stdio.h>
#include<math.h>
int triangle_area(int a,int b,int c){
    int sum=a+b;
    if(sum>c){
        return (a*b)/2;
    }
    else{
        return -1;
    }
}
int main()
{
    int a,b,c;
    scanf("%d%d%d",&a,&b,&c);
    printf("%d",triangle_area(a,b,c));
    return 0;
}

