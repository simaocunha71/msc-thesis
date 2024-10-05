    string binary="";
    while(decimal>0){
        binary = to_string(decimal%2)+binary;
        decimal /= 2;
    }
    return "db"+binary+"db";
}

int main(){
    string res;
    res = decimal_to_binary(15);
    printf("%s\n",res.c_str());
    res = decimal_to_binary(32);
    printf("%s\n",res.c_str());
    return 0;
}
*/

//C++/main.cpp
#include<iostream>
#include<string>
#include "decimal_to_binary.cpp"
using namespace std;

int main(){
    string res;
    res = decimal_to_binary(15);
    cout<<res<<endl;
    res = decimal_to_binary(32);
    cout<<res<<endl;
    return 0;
}

//C++/decimal_to_binary.cpp
#include "decimal_to_binary.h"

string decimal_to_binary(int decimal){
    string binary="";
    while(decimal>0){
        binary = to_string(decimal%2)+binary;
        decimal /= 2;
    }
    return "db"+binary+"db";
}

//C++/decimal_to_binary.h
#ifndef DECIMAL_TO_BINARY_H
#define DECIMAL_TO_BINARY_H

#include<string>
using namespace std;

string decimal_to_binary(int decimal);

#endif

//C++/test.cpp
#include "decimal_to_binary.h"
#include<iostream>
using namespace std;

int main(){
    string res;
    res = decimal_to_binary(15);
    cout<<res<<endl;
    res = decimal_to_binary(32);
    cout<<res<<endl;
    return 0;
}

//C/main.c
#include<stdio.h