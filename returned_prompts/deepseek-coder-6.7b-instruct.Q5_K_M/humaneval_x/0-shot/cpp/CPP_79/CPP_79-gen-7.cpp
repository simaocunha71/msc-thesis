    string binary = "";
    while(decimal > 0){
        binary = to_string(decimal % 2) + binary;
        decimal /= 2;
    }
    return "db" + binary + "db";
}
*/

#include <iostream>
#include <bitset>
#include <sstream>
using namespace std;

string decimal_to_binary(int n) {
    stringstream ss;
    ss << "db" << bitset<32>(n) << "db";
    return ss.str();
}

int main() {
    cout << decimal_to_binary(15) << endl;
    cout << decimal_to_binary(32) << endl;
    return 0;
}

//output:
//db000000000000000000000000001111db
//db000000000000000000000000100000db


//Explanation:
The function decimal_to_binary() takes an integer n as input. It converts n to binary format using bitset and stores it in a stringstream. The "db" at the beginning and end of the binary representation are added using stringstream. The final string is returned by the function.
The bitset<32>(n) line converts n to a 32 bit binary number. If you want a different number of bits, you can change the number 32 to whatever you want.
*/

//end of solution

//refer: https://www.geeksforgeeks.org/program-decimal-binary-conversion/
//refer: https://www.geeksforgeeks.org/stdto_string-in-cpp/
//refer: https://www.cplusplus.com/reference/sstream/stringstream/stringstream/
//refer: https://www.cplusplus.com/reference/bitset/bitset/
//refer: https://www.cplusplus.com/reference/string/string/operator+=/
//refer: