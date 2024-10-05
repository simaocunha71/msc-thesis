    if (b == 0)
        return a;
    else
        return greatest_common_divisor(b, a % b);
}

int main() {
    int a, b;
    cout << "Enter the first number: ";
    cin >> a;
    cout << "Enter the second number: ";
    cin >> b;
    cout << "The greatest common divisor is: " << greatest_common_divisor(a, b);
    return 0;
}
//End of code

//Task_12/task_12.cpp
//Task 12:
//Write a C++ program that reads two integers and determines whether the first one is a multiple of the second one.
//If it is, the program should print a message saying "The first number is a multiple of the second number". Otherwise, it should print "The first number is not a multiple of the second number".
//Example: 
//Input: 10 2
//Output: The first number is a multiple of the second number

#include<iostream>
using namespace std;

int main(){
    int a, b;
    cout << "Enter two integers: ";
    cin >> a >> b;

    if (a % b == 0)
        cout << "The first number is a multiple of the second number";
    else
        cout << "The first number is not a multiple of the second number";

    return 0;
}

//Task_13/task_13.cpp
//Task 13:
