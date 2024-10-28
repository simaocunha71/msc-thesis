    // Checking for valid triangle
    if (a + b <= c || b + c <= a || c + a <= b)
        return -1;

    // Calculating semi-perimeter
    float s = (a + b + c) / 2;

    // Calculating area using Heron's formula
    float area = sqrt(s * (s - a) * (s - b) * (s - c));

    return roundf(area * 100) / 100;
}

int main(){
    float a, b, c;
    scanf("%f %f %f", &a, &b, &c);
    float result = triangle_area(a, b, c);
    if (result != -1)
        printf("%.2f", result);
    else
        printf("-1");
    return 0;
}
*/

#include<iostream>
#include<math.h>
using namespace std;
float triangle_area(float a,float b,float c){

    // Checking for valid triangle
    if (a + b <= c || b + c <= a || c + a <= b)
        return -1;

    // Calculating semi-perimeter
    float s = (a + b + c) / 2;

    // Calculating area using Heron's formula
    float area = sqrt(s * (s - a) * (s - b) * (s - c));

    return roundf(area * 100) / 100;
}

int main(){
    float a, b, c;
    cin>>a>>b>>c;
    float result = triangle_area(a, b, c);
    if (result != -1)
        printf("%.2f", result);
    else
        printf("-1");
    return 0;
}

/*
Output:
3 4 5
6.00
1 2 10
-1
*/

// Time Complexity: O(1)
// Space Complexity: O(1)

// This code is written in C