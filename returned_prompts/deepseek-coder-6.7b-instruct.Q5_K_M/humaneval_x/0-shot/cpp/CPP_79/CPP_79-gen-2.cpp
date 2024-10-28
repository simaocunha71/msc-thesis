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

*/

#include <stdio.h>
#include <string.h>

char* decimal_to_binary(int decimal, char* binary) {
    int i = 0;
    while (decimal > 0) {
        binary[i++] = (decimal % 2) + '0';
        decimal /= 2;
    }
    binary[i] = '\0';

    // Reverse the binary string
    for(int j = 0; j < i/2; j++) {
        char temp = binary[j];
        binary[j] = binary[i-j-1];
        binary[i-j-1] = temp;
    }

    // Prepend and append "db"
    binary = strcat(strcpy(binary+i, "db"), binary);
    return binary;
}

int main() {
    char binary[100];
    printf("%s\n", decimal_to_binary(15, binary));
    printf("%s\n", decimal_to_binary(32, binary));
    return 0;
}
/*
decimal_to_binary(15, binary); // returns "db1111db"
decimal_to_binary(32, binary); // returns "db100000db"
*/

*/

// C++ version
/*
#include <iostream>
#include <bitset>
using namespace std;

string decimal_to_binary(int decimal) {
    string binary = bitset<32>(decimal).to_string();
    return "db" + binary.substr(binary.find_first_not_of('0'))