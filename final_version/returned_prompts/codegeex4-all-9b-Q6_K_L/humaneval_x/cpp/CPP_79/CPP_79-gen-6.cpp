/*
The decimal_to_binary() function in C++ is used to convert a decimal number to its binary representation. 

Here is a step-by-step breakdown of the function:

1. The function takes an integer decimal as an input.

2. The function converts the decimal number to its binary representation using the built-in function to_string().

3. The function then adds the characters "db" at the beginning and the end of the string.

4. The function then returns the resulting string.

The function is declared as a string, because the binary representation of a decimal number is a string. 

The function uses the to_string() function to convert the decimal number to a string. 

The to_string() function is a built-in function in C++ that converts a number to a string. 

The to_string() function takes a number as an input and returns a string representing that number. 

The function then adds the characters "db" at the beginning and the end of the string. 

The function then returns the resulting string.
*/
#include <string>
using namespace std;

string decimal_to_binary(int decimal) {
    string binary = to_string(decimal);
    binary = "db" + binary + "db";
    return binary;
}