#include <iostream>
#include <string>

using namespace std;

string decimal_to_binary(int decimal) {
    string result = "db";
    while (decimal > 0) {
        result += (decimal % 2 == 0 ? "0" : "1");
        decimal /= 2;
    }
    reverse(result.begin() + 2, result.end());
    result += "db";
    return result;
}

int main() {
    cout << decimal_to_binary(15) << endl;   // returns "db1111db"
    cout << decimal_to_binary(32) << endl;   // returns "db100000db"
    return 0;
}

