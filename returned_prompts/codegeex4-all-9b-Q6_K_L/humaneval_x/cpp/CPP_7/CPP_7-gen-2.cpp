```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> filter_by_substring(vector<string> strings, string substring) {
    vector<string> result;
    for (const auto& str : strings) {
        if (str.find(substring) != string::npos) {
            result.push_back(str);
        }
    }
    return result;
}

int main() {
    vector<string> strings = {"abc", "bacd", "cde", "vector"};
    string substring = "a";
    vector<string> filteredStrings = filter_by_substring(strings, substring);
    for (const auto& str : filteredStrings) {
        cout << str << endl;
    }
    return 0;
}
```
This code defines a function `filter_by_substring` that takes a vector of strings and a substring as input and returns a new vector containing only the strings from the input that contain the given substring. The function iterates over each string in the input vector, uses the `find` method to check if the substring is present in the string, and if so, adds the string to the result vector. The `main` function demonstrates how to use the `filter_by_substring` function and prints the filtered strings to the console.