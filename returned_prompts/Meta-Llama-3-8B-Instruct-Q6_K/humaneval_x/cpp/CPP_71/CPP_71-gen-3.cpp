    if(a+b>c && a+c>b && b+c>a)
    {
        float s=(a+b+c)/2.0;
        float area=sqrt(s*(s-a)*(s-b)*(s-c));
        return round(area*100.0)/100.0;
    }
    else
    {
        return -1.0;
    }
}
int main()
{
    printf("%.2f\n",triangle_area(3,4,5));
    printf("%.2f\n",triangle_area(1,2,10));
    return 0;
}
B:
#include<iostream>
#include<cmath>
using namespace std;
float triangle_area(float a, float b, float c) {
    if (a + b > c && a + c > b && b + c > a) {
        float s = (a + b + c) / 2.0;
        float area = sqrt(s * (s - a) * (s - b) * (s - c));
        return round(area * 100.0) / 100.0;
    } else {
        return -1.0;
    }
}

int main() {
    cout << fixed << setprecision(2) << triangle_area(3, 4, 5) << endl;
    cout << fixed << setprecision(2) << triangle_area(1, 2, 10) << endl;
    return 0;
}
C:
#include <iostream>
#include <cmath>
using namespace std;

float triangle_area(float a, float b, float c) {
    if (a + b > c && a + c > b && b + c > a) {
        float s = (a + b + c) / 2.0;
        float area = sqrt(s * (s - a) * (s - b) * (s - c));
        return round(area * 100.0) / 100.0;
    } else {
        return -1.0;
    }
}

int main() {
    cout << setprecision(2) << triangle_area(3, 4, 5) << endl;
    cout << setprecision(2) << triangle_area(1, 2, 10) << endl;
    return 0;
}
D:
#include <iostream>
#include <cmath>
using namespace std;

float triangle_area(float a, float b, float c) {
    if (a + b > c && a + c > b