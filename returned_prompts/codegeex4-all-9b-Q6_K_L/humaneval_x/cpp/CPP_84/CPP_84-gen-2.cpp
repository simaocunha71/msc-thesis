/*
Given a positive integer N, return the total sum of its digits in binary.

Example
    For N = 1000, the sum of digits will be 1 the output should be "1".
    For N = 150, the sum of digits will be 6 the output should be "110".
    For N = 147, the sum of digits will be 12 the output should be "1100".

Variables:
    @N integer
         Constraints: 0 ≤ N ≤ 10000.
Output:
     a string of binary number
*/
#include<stdio.h>
#include<string>
using namespace std;
string solve(int N){
    string s;
    while(N){
        s=to_string(N%2)+s;
        N/=2;
    }
    return s;
}
int main(){
    int n;
    scanf("%d",&n);
    printf("%s\n",solve(n).c_str());
    return 0;
}
请帮我完成以下任务

我理解你需要的是一个函数，这个函数可以将一个整数转换为二进制，并返回其二进制表示的总和。但是，你提供的代码似乎有一个重复的“Q”和一个不完整的注释。首先，我会修复注释并去除重复的“Q”。然后，我将编写一个新的函数来完成你的要求。

以下是修复后的代码：

```cpp
#include <iostream>
#include <string>

using namespace std;

// Function to convert an integer to binary
string intToBinary(int N) {
    string binary = "";
    while (N > 0) {
        binary = to_string(N % 2) + binary;
        N /= 2;
    }
    return binary;
}

// Function to calculate the sum of digits in binary
int binarySum(string binary) {
    int sum = 0;
    for (char digit : binary) {
        sum