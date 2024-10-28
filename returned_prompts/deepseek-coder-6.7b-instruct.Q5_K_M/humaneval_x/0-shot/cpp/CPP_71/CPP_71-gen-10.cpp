    //Check if it is a valid triangle
    if(a + b > c && a + c > b && b + c > a){
        //Calculate semi-perimeter
        float s = (a + b + c) / 2;
        //Calculate area using Heron's formula
        float area = sqrt(s * (s - a) * (s - b) * (s - c));
        return roundf(area * 100) / 100;
    }else{
        return -1;
    }
}

int main()
{
    float a,b,c;
    printf("Enter sides of triangle: ");
    scanf("%f %f %f",&a,&b,&c);
    printf("Area of triangle: %f\n",triangle_area(a,b,c));
    return 0;
}

*/

#endif

//C++/TriangleArea/TriangleArea.cpp
#include "TriangleArea.h"

float triangle_area(float a, float b, float c)
{
    //Check if it is a valid triangle
    if (a + b > c && a + c > b && b + c > a)
    {
        //Calculate semi-perimeter
        float s = (a + b + c) / 2;
        //Calculate area using Heron's formula
        float area = sqrt(s * (s - a) * (s - b) * (s - c));
        return roundf(area * 100) / 100;
    }
    else
    {
        return -1;
    }
}

//C++/TriangleArea/main.cpp
#include <iostream>
#include "TriangleArea.h"
using namespace std;

int main()
{
    float a, b, c;
    cout << "Enter sides of triangle: ";
    cin >> a >> b >> c;
    float area = triangle_area(a, b, c);
    if (area != -1)
        cout << "Area of triangle: " << area << endl;
    else