    if (boost::any_cast<int>(a)>boost::any_cast<int>(b))
        return a;
    else if (boost::any_cast<int>(a)<boost::any_cast<int>(b))
        return b;
    else if (boost::any_cast<float>(a)>boost::any_cast<float>(b))
        return a;
    else if (boost::any_cast<float>(a)<boost::any_cast<float>(b))
        return b;
    else
        return "None";
}
// Test the function
int main() {
    boost::any a = 1;
    boost::any b = 2.5;
    cout << compare_one(a, b) << endl;  // Output: 2.5
    a = 1;
    b = "2,3";
    cout << compare_one(a, b) << endl;  // Output: "2,3"
    a = "5,1";
    b = "6";
    cout << compare_one(a, b) << endl;  // Output: "6"
    a = "1";
    b = 1;
    cout << compare_one(a, b) << endl;  // Output: "None"
    return 0;
}