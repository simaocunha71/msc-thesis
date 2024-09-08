

C++:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

vector<string> sorted_list_sum(vector<string> lst) {
    vector<string> result;
    // Delete the strings that have odd lengths from the list
    for (const auto &word : lst) {
        if (word.length() % 2 == 0) {
            result.push_back(word);
        }
    }
    // Sort the resulted vector
    sort(result.begin(), result.end(), [](const string &a, const string &b) {
        if (a.length() == b.length()) {
            return a < b;
        }
        return a.length() < b.length();
    });
    return result;
}

int main() {
    vector<string> lst = {"aa", "a", "aaa", "cd", "ab"};
    vector<string> result = sorted_list_sum(lst);
    for (const auto &word : result) {
        cout << word << " ";
    }
    cout << endl;
    return 0;
}
```

Output:
```
aa ab cd
```

Explanation:
The function `sorted_list_sum` takes a vector of strings as input, removes the strings with odd lengths, and returns the resulted vector sorted by the length of the strings. If two strings have the same length, they are sorted alphabetically. The main function demonstrates the usage of the `sorted_list_sum` function with a sample input and prints the output. The output is a vector of strings sorted by the length of the strings, and then alphabetically if the lengths are the same.