
}

int main() {
    printf("%d\n", closest_integer("10"));
    printf("%d\n", closest_integer("15.3"));
    printf("%d\n", closest_integer("14.5"));
    printf("%d\n", closest_integer("-14.5"));
    return 0;
}
*/


A: Here is the C++ solution for your problem.

#include<iostream>
#include<cmath>
#include<string>
using namespace std;

int closest_integer(string value) {
    double num = stod(value);
    int rounded_num = round(num);
    if(fabs(num - rounded_num) < 0.5)
        return num > 0 ? rounded_num : rounded_num - 1;
    else
        return rounded_num;
}

int main() {
    cout << closest_integer("10") << "\n";
    cout << closest_integer("15.3") << "\n";
    cout << closest_integer("14.5") << "\n";
    cout << closest_integer("-14.5") << "\n";
    return 0;
}


This solution uses stod() function to convert string to double. Then it uses round() function to round the number to the nearest integer. If the absolute difference between the original number and its rounded version is less than 0.5, it rounds away from zero by returning the number rounded to the nearest integer minus 1 if the original number is negative. If the absolute difference is not less than 0.5, it just returns the rounded number.

A: Here's a Python solution that uses the built-in round function and the float function to convert the string to a number.

def closest_integer(value):
    num = float(value)
    rounded_num = round(num)
    if abs(num - rounded_num) < 0.5:
        return rounded_num if num > 0 else rounded_num - 1
    else:
        return rounded_num

print(closest_integer("10"))
print(closest_integer("15.3"))
print(clos