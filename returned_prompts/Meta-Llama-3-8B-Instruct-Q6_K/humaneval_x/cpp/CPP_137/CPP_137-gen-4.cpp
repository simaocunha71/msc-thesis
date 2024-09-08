```cpp
#include <iostream>
#include <boost/any.hpp>
#include <string>
#include <limits>
#include <cctype>

using namespace std;
using namespace boost;

any compare_one(any a, any b) {
    if (a.type() == typeid(int) && b.type() == typeid(int)) {
        int x = boost::any_cast<int>(a);
        int y = boost::any_cast<int>(b);
        if (x > y) return a;
        else if (x < y) return b;
        else return any(typeid(string)); // Return "None" as a string
    } else if (a.type() == typeid(double) && b.type() == typeid(double)) {
        double x = boost::any_cast<double>(a);
        double y = boost::any_cast<double>(b);
        if (x > y) return a;
        else if (x < y) return b;
        else return any(typeid(string)); // Return "None" as a string
    } else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        string x = boost::any_cast<string>(a);
        string y = boost::any_cast<string>(b);

        // Check if the strings represent real numbers
        bool x_is_real = false;
        bool y_is_real = false;
        for (char c : x) {
            if (c == '.' || c == ',') x_is_real = true;
        }
        for (char c : y) {
            if (c == '.' || c == ',') y_is_real = true;
        }

        if (x_is_real && y_is_real) {
            double x_num = stod(x);
            double y_num = stod(y);
            if (x_num > y_num) return a;
            else if (x_num < y_num) return b;
            else return any(typeid(string)); // Return "None" as a string
        } else {
            return x_is_real ? a : b;
        }
    } else {
        throw invalid_argument("Invalid types");
    }
}

int main() {
    any a = 1;
    any b = 2.5;
    cout << boost::any_cast<any>(compare_one(a, b)) << endl; // Output: 2.5

    a = 1;
    b = "2,3";
    cout << boost::any_cast<any>(compare_one(a,