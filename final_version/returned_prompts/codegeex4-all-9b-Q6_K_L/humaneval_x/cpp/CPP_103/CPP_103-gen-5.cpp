#include <cmath>
#include <iostream>
#include <string>
using namespace std;

string rounded_avg(int n, int m) {
    if (n > m) {
        return "-1";
    }

    double sum = 0;
    int count = 0;
    for (int i = n; i <= m; i++) {
        sum += i;
        count++;
    }

    double avg = sum / count;
    int rounded = floor(avg + 0.5);
    return bitset<8>(rounded).to_string();
}

int main() {
    cout << rounded_avg(1, 5) << endl;  // "11"
    cout << rounded_avg(7, 5) << endl;  // "-1"
    cout << rounded_avg(10, 20) << endl;  // "1111"
    cout << rounded_avg(20, 33) << endl;  // "11010"
    return 0;
}

