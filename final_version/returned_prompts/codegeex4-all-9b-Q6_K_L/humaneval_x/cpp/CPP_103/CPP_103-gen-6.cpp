```cpp
#include <bits/stdc++.h>
using namespace std;

string rounded_avg(int n, int m) {
    if (n > m) return "-1";
    double avg = ((double)n + m) / 2;
    int rounded_avg = floor(avg);
    string binary = bitset<32>(rounded_avg).to_string();
    int len = binary.size();
    for (int i = 0; i < len; i++) {
        if (binary[i] == '1') {
            binary = binary.substr(i);
            break;
        }
    }
    return binary;
}
int main() {
    cout << rounded_avg(1, 5) << "\n";  // Output: "11"
    cout << rounded_avg(7, 5) << "\n";  // Output: "-1"
    cout << rounded_avg(10, 20) << "\n";  // Output: "1111"
    cout << rounded_avg(20, 33) << "\n";  // Output: "11010"
    return 0;
}
```