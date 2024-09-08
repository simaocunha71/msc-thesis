int digits(int n){
    int product = 1;
    int count = 0;
    int flag = 0; //flag to check if all digits are even
    int temp = n;
    while(temp){
        int digit = temp % 10;
        if(digit % 2 == 0){
            flag = 1;
        }
        else{
            product *= digit;
            count++;
        }
        temp /= 10;
    }
    if(flag == 1 && count == 0){
        return 0;
    }
    else{
        return product;
    }
}

B:
#include <iostream>
#include <string>

int digits(int n) {
    string s = to_string(n);
    int product = 1;
    for (char c : s) {
        int digit = c - '0';
        if (digit % 2 != 0) {
            product *= digit;
        }
    }
    return product;
}

C:
#include <iostream>
#include <string>

int digits(int n) {
    string s = to_string(n);
    int product = 1;
    for (char c : s) {
        int digit = c - '0';
        if (digit % 2 != 0) {
            product *= digit;
        }
    }
    return product;
}

D:
#include <iostream>
#include <string>

int digits(int n) {
    string s = to_string(n);
    int product = 1;
    for (char c : s) {
        int digit = c - '0';
        if (digit % 2 != 0) {
            product *= digit;
        }
    }
    return product;
}

E:
#include <iostream>
#include <string>

int digits(int n) {
    string s = to_string(n);
    int product = 1;
    for (char c : s) {
        int digit = c - '0';
        if (digit % 2 != 0) {
            product *= digit;
        }
    }
    return product;
}

F:
#include <iostream>
#include <string>

int digits(int n) {
    string s = to_string(n);
    int product = 1;
    for (char c : s) {
        int digit = c - '0';
        if (digit % 2 != 0) {
            product *= digit;
        }
    }
    return product;
}

G:
#include <iostream>
#include <string>

int digits(int