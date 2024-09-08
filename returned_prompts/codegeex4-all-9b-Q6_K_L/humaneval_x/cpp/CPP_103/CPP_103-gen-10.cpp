#include <cmath>
#include <string>

string rounded_avg(int n, int m) {
    if (n > m) {
        return "-1";
    }
    double avg = round((n + m) / 2.0);
    int rounded = static_cast<int>(avg);
    string binary = "";
    while (rounded > 0) {
        binary = to_string(rounded % 2) + binary;
        rounded /= 2;
    }
    return binary.empty() ? "0" : binary;
}
