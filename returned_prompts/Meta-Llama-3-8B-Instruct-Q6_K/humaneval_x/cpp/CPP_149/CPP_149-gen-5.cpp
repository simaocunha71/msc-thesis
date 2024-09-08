    vector<string> result;
    sort(lst.begin(), lst.end(), [](const string& a, const string& b) {
        if (a.size() == b.size()) {
            return a < b;
        }
        return a.size() < b.size();
    });
    for (const auto& str : lst) {
        if (str.size() % 2 == 0) {
            result.push_back(str);
        }
    }
    return result;
}  



C++ Solution:
```cpp
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> sorted_list_sum(vector<string> lst) {
    vector<string> result;
    sort(lst.begin(), lst.end(), [](const string& a, const string& b) {
        if (a.size() == b.size()) {
            return a < b;
        }
        return a.size() < b.size();
    });
    for (const auto& str : lst) {
        if (str.size() % 2 == 0) {
            result.push_back(str);
        }
    }
    return result;
}
```

Explanation:

1.  The function `sorted_list_sum` takes a vector of strings as input.
2.  It first creates an empty vector `result` to store the filtered and sorted strings.
3.  The `sort` function is used to sort the input vector `lst` in ascending order based on the length of each string. If two strings have the same length, they are sorted alphabetically. This is achieved by providing a lambda function as the third argument to the `sort` function.
4.  The lambda function compares two strings `a` and `b` based on their lengths. If they have the same length, it returns `a < b`, which means that the strings are sorted alphabetically. If they have different lengths, it returns `a.size() < b.size()`, which means that the strings are sorted based on their lengths.
5.  After sorting the input vector, the function iterates over the sorted vector and checks each string's length using the modulo operator (`%`). If the length is even (i.e., `str.size() % 2 == 0`), the string is added to the `result` vector.
6.  Finally, the function returns the `result` vector, which contains the filtered and sorted strings.

The provided unit tests ensure that the function works correctly:

*   `assert vector_sort({"aa", "