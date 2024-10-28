    return fmod(number, 1);
}
int main() {
    float number;
    printf("Enter a positive floating point number: ");
    scanf("%f", &number);
    printf("Decimal part of the number: %.2f", truncate_number(number));
    return 0;
}

The program prompts the user for a number, sends it to the function 'truncate_number' which uses the fmod function from the math library to return the decimal part of the number. Then it prints the decimal part of the number.
*/

//C++/C++_Programs/Q7.cpp
#include<iostream>
using namespace std;

int main(){
    //