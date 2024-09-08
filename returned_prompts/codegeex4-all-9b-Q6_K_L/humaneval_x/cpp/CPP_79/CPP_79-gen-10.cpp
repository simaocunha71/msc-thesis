#include <bits/stdc++.h>
using namespace std;

string decimal_to_binary(int decimal){
    string binary = "";
    while(decimal > 0){
        binary = to_string(decimal % 2) + binary;
        decimal /= 2;
    }
    return "db" + binary + "db";
}

int main() {
    cout << decimal_to_binary(15) << endl;
    cout << decimal_to_binary(32) << endl;
    return 0;
}
