    string binary = "db";
    while(decimal > 0){
        binary = to_string(decimal % 2) + binary;
        decimal /= 2;
    }
    return binary + "db";
}

int main(){
    printf("%s\n", decimal_to_binary(15).c_str());
    printf("%s\n", decimal_to_binary(32).c_str());
    return 0;
}
*/

// C++ program to convert decimal to binary
#include<bits/stdc++.h>
using namespace std;

string decimalToBinary(int n)
{
    string binary = "db";
    for (int i = 31; i >= 0; i--) {
        binary += ((n >> i) & 1) ? '1' : '0';
    }
    return binary + "db";
}

int main()
{
    int n;
    n = 15;
    cout << decimalToBinary(n) << "\n";
    n = 32;
    cout << decimalToBinary(n) << "\n";
    return 0;
}

/*
This C++ program works by shifting the bits of the input decimal number by 31 to 0 positions and checking if each bit is set or not. If the bit is set, a '1' is appended to the binary string, otherwise a '0' is appended. This process is repeated until all bits are processed. Finally, the binary string is appended with "db" at the beginning and end and returned.
*/

// C++ program to convert decimal to binary
#include<bits/stdc++.h>
using namespace std;

string decimalToBinary(int n)
{
    string binary = "db";
    for (int i = 31; i >= 0; i--) {
        binary += ((n >> i) & 1) ? '1' : '0';
    }
    return binary + "db";
}

int main()
{
    int n;
    n = 15;
    cout << decimalToBinary(n) << "\n";
    n = 32;
    cout << decimal