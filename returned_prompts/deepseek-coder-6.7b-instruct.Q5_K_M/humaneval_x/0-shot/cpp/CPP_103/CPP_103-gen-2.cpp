    if(n > m) return "-1";

B:
    Compute the sum of integers from n through m (including n and m).
C:
    Compute the average of these integers. Round the result to the nearest integer.
D:
    Convert this average to binary representation.
*/

// Code
#include <bits/stdc++.h>
using namespace std;

string rounded_avg(int n, int m) {
    if(n > m) return "-1";

    int sum = 0;
    for(int i = n; i <= m; i++) {
        sum += i;
    }

    int avg = round((double)sum/(m-n+1));

    stringstream ss;
    ss << bitset<32>(avg);
    return ss.str();
}

int main() {
    int n = 20, m = 33;
    cout << rounded_avg(n, m) << endl;
    return 0;
}


This code first checks if n is greater than m. If so, it returns "-1". It then calculates the sum of integers from n to m (inclusive). It computes the average of these integers and rounds it to the nearest integer. Finally, it converts this average to binary representation and returns it.

Please note that the bitset<32>(avg) converts the integer 'avg' to a binary string. The number