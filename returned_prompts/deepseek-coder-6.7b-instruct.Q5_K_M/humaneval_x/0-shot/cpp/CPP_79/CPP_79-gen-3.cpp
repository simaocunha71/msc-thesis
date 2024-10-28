    string binary = "";
    while(decimal > 0){
        binary = to_string(decimal % 2) + binary;
        decimal /= 2;
    }
    return "db" + binary + "db";
}

int main(){
    printf("%s\n", decimal_to_binary(15).c_str());
    printf("%s\n", decimal_to_binary(32).c_str());
    return 0;
}

// The algorithm works by dividing the decimal number by 2 and storing the remainder.
// This remainder is appended to the start of the binary string. The process is repeated
// with the result of the division until the decimal number becomes 0. At the end,
// the binary string is prefixed and suffixed with "db" to satisfy the problem's formatting
// requirements.
//
// The time complexity of this algorithm is O(log(n)), where n is the decimal number.
// This is because the decimal number is divided by 2 in each iteration until it becomes 0.
// The space complexity is also O(log(n)), because a binary string of length log(n) is created.
// The space complexity does not include the space needed for the output string, which is a
// constant amount of space.
//
// This solution assumes that the input will always be a positive integer. If negative numbers
// or non-integer values are possible inputs, additional error checking or input validation
// should be added.
//
// This solution also assumes that the input number is small enough to fit in an integer.
// If the input number could be larger than an integer, the solution should be modified to use
// a larger data type to store the input number.
//
// This solution uses C++ and the standard library, so it can be compiled and run with a C++ compiler.
// The function decimal_to_binary takes an integer as an argument and returns a string. The main
// function tests the decimal_to_binary function with the numbers 15 and 32.
// The to_string function is used to convert the integer remainder to a string before appending
// it to the binary string. The binary string is then prefixed and suffixed with "db" before
// being returned.
// The