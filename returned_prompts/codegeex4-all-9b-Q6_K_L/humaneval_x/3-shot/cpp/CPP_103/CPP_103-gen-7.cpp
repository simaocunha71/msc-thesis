
The last question is about the average of the integers from n through m. You are returning the string representation of the integer average. You should return the string representation of the binary average. You can convert the integer to binary using std::bitset or std::bitset::to_string.
For example, you can use std::bitset to convert the integer to a binary string:
#include <bitset>

std::string rounded_avg(int n, int m) {
    if (n > m)
        return "-1";
    int avg = (n + m) / 2;
    std::bitset<8> binary(avg);
    return binary.to_string();
}

Note that the bitset size is 8, which means it will represent the binary representation of an integer with up to 8 bits. If you want to represent integers with more bits, you can increase the bitset size.