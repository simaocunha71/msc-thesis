    if(n>m) return "-1";

B:
    int avg = (int)round((n+m)/2.0);

C:
    return bitset<32>(avg).to_string();
}

int main(){
    printf("%s\n", rounded_avg(1, 5).c_str());
    printf("%s\n", rounded_avg(7, 5).c_str());
    printf("%s\n", rounded_avg(10, 20).c_str());
    printf("%s\n", rounded_avg(20, 33).c_str());
    return 0;
}
*/

#include <iostream>
#include <cmath>
#include <bitset>

std::string rounded_avg(int n, int m){
    if(n > m){
        return "-1";
    }

    int avg = std::round((n + m) / 2.0);
    std::string binary = std::bitset<32>(avg).to_string();
    // Remove leading zeros
    binary = binary.substr(binary.find_first_not_of('0'));

    return binary;
}

int main(){
    std::cout << rounded_avg(1, 5) << std::endl;
    std::cout << rounded_avg(7, 5) << std::endl;
    std::cout << rounded_avg(10, 20) << std::endl;
    std::cout << rounded_avg(20, 33) << std::endl;

    return 0;
}

/*
Test Cases:
Input: 1, 5
Output: "11"

Input: 7, 5
Output: "-1"

Input: 10, 20
Output: "1111"

Input: 20, 33
Output: "11010"
*/

// Problem 2: Fibonacci Sequence - Find nth Fibon