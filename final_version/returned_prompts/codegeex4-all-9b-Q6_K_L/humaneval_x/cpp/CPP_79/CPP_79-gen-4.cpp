#include <iostream>
using namespace std;
string decimal_to_binary(int decimal){
    string result = "db";
    while(decimal > 0){
        result += to_string(decimal % 2);
        decimal /= 2;
    }
    reverse(result.begin(), result.end());
    result += "db";
    return result;
}
int main() {
    cout << decimal_to_binary(15) << endl;
    cout << decimal_to_binary(32) << endl;
    return 0;
}