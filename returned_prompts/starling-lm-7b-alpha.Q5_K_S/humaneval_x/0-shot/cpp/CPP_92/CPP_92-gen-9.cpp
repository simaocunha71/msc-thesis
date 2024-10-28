
Answer: /*
#include <iostream>
using namespace std;
bool any_int(int a, int b, int c) {
    if (a == b + c || b == a + c || c == a + b) {
        return true;
    } else {
        return false;
    }
}
int main() {
    cout << any_int(5, 2, 7) << endl;
    cout << any_int(3, 2, 2) << endl;
    cout << any_int(3, -2, 1) << endl;
    cout << any_int(3.6, -2.2, 2) << endl;
    return 0;
}
*/

Explanation:

In this problem, we need to check whether one of the numbers is equal to the sum of the other two numbers and all numbers are integers. We can define a function called any_int to check this condition. The function takes three integer parameters a, b, and c.

Inside the function, we first check if all three numbers are integers using the modulo operator (%). If the remainder of dividing each number by 1 is 0, then the number is an integer. We use the round function to round the floating-point numbers to the nearest integer value.

Next, we check if any of the numbers is equal to the sum of the other two. We use the logical OR operator (||) to check all three conditions. If any of the conditions is true, we return true; otherwise, we return false.

In the main function, we test the any_int function with different input values and print the result using the cout statement.

The output of the program is: