    if((a+b>c) && (a+c>b) && (b+c>a))
    {
        float s = (a+b+c)/2;
        float area = sqrt(s*(s-a)*(s-b)*(s-c));
        return roundf(area*100.0)/100.0;
    }
    else
    {
        return -1;
    }
}  // A: stands for Answer
// C++ implementation of the above problem
// This program calculates the area of a triangle given the lengths of its sides.

int main() {
    printf("%.2f\n", triangle_area(3.0, 4.0, 5.0));  // 6.00
    printf("%.2f\n", triangle_area(1.0, 2.0, 10.0)); // -1.00
    return 0;
}

// Output:
// 6.00
// -1.00

// The triangle_area function first checks if the given sides can form a valid triangle. 
// If they can, it calculates the area of the triangle using Heron's formula and returns it. 
// If they cannot, it returns -1. The roundf function is used to round the area to 2 decimal places. 
// In the main function, we test the triangle_area function with two sets of sides and print the results. 

// Time complexity: O(1) 
// Space complexity: O(1) 
// The time complexity is O(1) because the function performs a constant number of operations. 
// The space complexity is O(1) because the function uses a constant amount of space.  // A: stands for Answer
// C++ implementation of the above problem
// This program calculates the area of a triangle given the lengths of its sides.
#include<iostream>
using namespace std;
float triangle_area(float a,float b,float c){
    if((a+b>c) && (a+c>b) && (b+c>a))
    {
        float s = (a+b+c)/2;
        float area = sqrt(s*(s-a)*(s-b)*(s-c));
        return roundf(area*100.0)/100.0;
    }
    else
    {
        return -1;
    }
}
int main() {
    cout<<fixed<<setprecision(2);
    printf("%.2f\n", triangle_area(3.0, 4.0, 5.0));  // 6