#include <boost/any.hpp>
#include <string>
#include <algorithm>

using namespace std;

boost::any compare_one(boost::any a, boost::any b) {
    double da, db; // declare double variables
    string sa, sb; // declare string variables
    if (boost::any_cast<double>(a)) { // check if a is a double
        da = boost::any_cast<double>(a);
    } else if (boost::any_cast<string>(a)) { // check if a is a string
        sa = boost::any_cast<string>(a);
    } else {
        return "Invalid input"; // return error if a is neither double nor string
    }
    if (boost::any_cast<double>(b)) { // check if b is a double
        db = boost::any_cast<double>(b);
    } else if (boost::any_cast<string>(b)) { // check if b is a string
        sb = boost::any_cast<string>(b);
    } else {
        return "Invalid input"; // return error if b is neither double nor string
    }
    if (da > db) { // compare double values
        return a; // return the larger double value
    } else if (da < db) {
        return b; // return the larger double value
    } else if (sa > sb) { // compare string values
        return a; // return the larger string value
    } else if (sa < sb) {
        return b; // return the larger string value
    } else {
        return "None"; // return "None" if the values are equal
    }
}

int main() {
    boost::any a = 1;
    boost::any b = 2.5;
    cout << compare_one(a, b) << endl; // Output: 2.5
    a = "5,1";
    b = "6";
    cout << compare_one(a, b) << endl; // Output: 6
    a = "1";
    b = 1;
    cout << compare_one(a, b) << endl; // Output: None
    return 0;
}
