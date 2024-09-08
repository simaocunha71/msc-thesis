    if(a+b>c && a+c>b && b+c>a){
        float s = (a+b+c)/2;
        float area = sqrt(s*(s-a)*(s-b)*(s-c));
        return roundf(area*100.0)/100.0;
    }
    else
        return -1.0;

} // end of function
int main()
{
    printf("%.2f\n",triangle_area(3, 4, 5)); // Should print 6.00
    printf("%.2f\n",triangle_area(1, 2, 10)); // Should print -1.00
    return 0;
}
B:
#include<stdio.h>
#include<math.h>
using namespace std;
float triangle_area(float a,float b,float c){
    if(a+b>c && a+c>b && b+c>a){
        float s = (a+b+c)/2;
        float area = sqrt(s*(s-a)*(s-b)*(s-c));
        return roundf(area*100.0)/100.0;
    }
    else
        return -1.0;
}
int main()
{
    printf("%.2f\n",triangle_area(3, 4, 5)); // Should print 6.00
    printf("%.2f\n",triangle_area(1, 2, 10)); // Should print -1.00
    return 0;
}
C:
#include<stdio.h>
#include<math.h>
using namespace std;
float triangle_area(float a,float b,float c)
{
    if(a+b<=c || a+c<=b || b+c<=a)
    {
        return -1.0;
    }
    else
    {
        float s = (a+b+c)/2;
        float area = sqrt(s*(s-a)*(s-b)*(s-c));
        return roundf(area*100.0)/100.0;
    }
}
int main()
{
    printf("%.2f\n",triangle_area(3, 4, 5)); // Should print 6.00
    printf("%.2f\n",triangle_area(1, 2, 10)); // Should print -1.00
    return 0;
}
D:
#include<stdio.h>
#include<math.h>
using namespace std;
float triangle_area(float a,float b,float c)
{
    if(a+b<=c || a+c<=b || b+c<=a)
    {
        return -1.0;
    }
    else
