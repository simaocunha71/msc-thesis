#include <iostream>
#include <string>
#include <algorithm>
#include <boost/any.hpp>

using namespace std;

// Function to compare two values
boost::any compareOne(boost::any a, boost::any b) {
    // If both values are integers
    if (boost::any_cast<int>(a) && boost::any_cast<int>(b)) {
        if (boost::any_cast<int>(a) > boost::any_cast<int>(b)) {
            return a;
        } else if (boost::any_cast<int>(a) < boost::any_cast<int>(b)) {
            return b;
        } else {
            return "None";
        }
    }
    // If both values are floats
    else if (boost::any_cast<float>(a) && boost::any_cast<float>(b)) {
        if (boost::any_cast<float>(a) > boost::any_cast<float>(b)) {
            return a;
        } else if (boost::any_cast<float>(a) < boost::any_cast<float>(b)) {
            return b;
        } else {
            return "None";
        }
    }
    // If both values are strings
    else if (boost::any_cast<string>(a) && boost::any_cast<string>(b)) {
        if (boost::any_cast<string>(a) > boost::any_cast<string>(b)) {
            return a;
        } else if (boost::any_cast<string>(a) < boost::any_cast<string>(b)) {
            return b;
        } else {
            return "None";
        }
    }
    // If one value is an integer and the other is a float
    else if (boost::any_cast<int>(a) && boost::any_cast<float>(b)) {
        if (static_cast<float>(boost::any_cast<int>(a)) > boost::any_cast<float>(b)) {
            return a;
        } else if (static_cast<float>(boost::any_cast<int>(a)) < boost::any_cast<float>(b)) {
            return b;
        } else {
            return "None";
        }
    }
    // If one value is a float and the other is an integer
    else if (boost::any_cast<float>(a) && boost::any_cast<int>(b)) {
        if (boost::any_cast<float>(a) > static_cast<float>(boost::any_cast<int>(b))) {
            return a;
        } else if (boost