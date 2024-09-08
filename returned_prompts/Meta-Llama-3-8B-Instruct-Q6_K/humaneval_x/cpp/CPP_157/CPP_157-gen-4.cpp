    if(a+b>c && a+c>b && b+c>a)
    {
        float c_square = pow(c,2);
        float a_square = pow(a,2);
        float b_square = pow(b,2);
        if(c_square == a_square+b_square)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }
}

int main()
{
    float a,b,c;
    printf("Enter the length of first side: ");
    scanf("%f",&a);
    printf("Enter the length of second side: ");
    scanf("%f",&b);
    printf("Enter the length of third side: ");
    scanf("%f",&c);
    if(right_angle_triangle(a,b,c))
    {
        printf("The three sides form a right-angled triangle.\n");
    }
    else
    {
        printf("The three sides do not form a right-angled triangle.\n");
    }
    return 0;
}

B:
#include <iostream>
#include <cmath>
using namespace std;

bool rightAngleTriangle(float a, float b, float c) {
    if (a + b > c && a + c > b && b + c > a) {
        float squareA = pow(a, 2);
        float squareB = pow(b, 2);
        float squareC = pow(c, 2);
        return (squareA == squareB + squareC || squareB == squareA + squareC || squareC == squareA + squareB);
    }
    return false;
}

int main() {
    float a, b, c;
    cout << "Enter the length of first side: ";
    cin >> a;
    cout << "Enter the length of second side: ";
    cin >> b;
    cout << "Enter the length of third side: ";
    cin >> c;
    if (rightAngleTriangle(a, b, c)) {
        cout << "The three sides form a right-angled triangle." << endl;
    } else {
        cout << "The three sides do not form a right-angled triangle." << endl;
    }
    return 0;
}

C:
#include <iostream>
#include <cmath>
using namespace std;

bool rightAngleTriangle(float a, float b, float c) {
    if (a * a + b * b == c * c || a * a + c * c == b * b || b *