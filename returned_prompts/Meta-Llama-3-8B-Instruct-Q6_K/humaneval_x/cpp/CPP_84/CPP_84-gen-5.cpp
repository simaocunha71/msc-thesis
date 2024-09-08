The problem is asking to find the total sum of the digits in the binary representation of a given number N. 

Here is a simple solution in C++:

```cpp
#include<stdio.h>
#include<string>
using namespace std;

string solve(int N) {
    int sum = 0;
    int n