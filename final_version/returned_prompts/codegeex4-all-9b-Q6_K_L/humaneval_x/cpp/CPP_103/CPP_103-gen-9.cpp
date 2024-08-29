#include <iostream>
#include <cmath>
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

    double average = sum / count;
    int rounded_average = floor(average + 0.5);

    return bitset<8>(rounded_average).to_string();
}

int main() {
    cout << rounded_avg(1, 5) << endl;  // 11
    cout << rounded_avg(7, 5) << endl;  // -1
    cout << rounded_avg(10, 20) << endl; // 1111
    cout << rounded_avg(20, 33) << endl; // 11010
    return 0;
}

C:
#include <iostream>
#include <cmath>
#include <bitset>

using namespace std;

string rounded_avg(int n, int m) {
    if (n > m) {
        return "-1";
    }

    long long sum = 0;
    int count = 0;

    for (int i = n; i <= m; i++) {
        sum += i;
        count++;
    }

    double average = static_cast<double>(sum) / count;
    int rounded_average = floor(average + 0.5);

    return bitset<8>(rounded_average).to_string();
}

int main() {
    cout << rounded_avg(1, 5) << endl;  // 11
    cout << rounded_avg(7, 5) << endl;  // -1
    cout << rounded_avg(10, 20) << endl; // 1111
    cout << rounded_avg(20, 33) << endl; // 11010
    return 0;
}

D:
#include <iostream>
#include <cmath>
#include <bitset>

using namespace std;

string rounded_avg(int n, int m) {
    if (n > m) {
        return "-1";
    }

    long long sum = 0;
    int count = 0;

    for (int i = n; i <= m; i++) {
        sum += i;
        count++;
    }

    double average = static_cast<double>(sum) / count;
    int rounded_average = floor(average