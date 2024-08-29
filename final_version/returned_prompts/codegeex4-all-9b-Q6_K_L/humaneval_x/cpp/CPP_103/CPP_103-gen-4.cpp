#include <iostream>
using namespace std;
#include <cmath>
#include <string>
string rounded_avg(int n, int m) {
    if (n > m) {
        return "-1";
    }
    // calculate the average of the range
    double average = (n + m) / 2.0;
    // round the average to the nearest integer
    int rounded = round(average);
    // convert the rounded integer to a binary string
    string binary = "";
    while (rounded > 0) {
        binary = to_string(rounded % 2) + binary;
        rounded /= 2;
    }
    // if the binary string is empty, return "0"
    if (binary.empty()) {
        return "0";
    }
    return binary;
}
int main() {
    cout << rounded_avg(1, 5) << endl; // should return "11"
    cout << rounded_avg(7, 5) << endl; // should return "-1"
    cout << rounded_avg(10, 20) << endl; // should return "1111"
    cout << rounded_avg(20, 33) << endl; // should return "11010"
    return 0;
}