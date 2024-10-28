    int count = 0, i;
    string prime_hex = "2357BDF";
    for (i = 0; i < num.size(); i++)
        if (prime_hex.find(num[i]) != string::npos) count++;
    return count;
}

int main(){
    string num;
    printf("Enter a Hexadecimal Number: ");
    getline(cin, num);
    printf("Number of prime Hexadecimal digits: %d", hex_key(num));
    return 0;
}

This program will take a hexadecimal number as an input from the user and print the number of prime hexadecimal digits in it. The function hex_key() checks each character in the input string and increments a counter if the character is a prime hexadecimal digit. The prime hexadecimal digits are 2, 3, 5, 7, B, D, F.
*/

#include<bits/stdc++.h>
using namespace