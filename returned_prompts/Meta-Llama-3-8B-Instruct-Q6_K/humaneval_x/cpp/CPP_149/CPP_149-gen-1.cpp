    vector<string> result;
    for (string s : lst) {
        if (s.length() % 2 == 0) {
            result.push_back(s);
        }
    }
    sort(result.begin(), result.end(), 
         [](const string& a, const string& b) {
             if (a.length() == b.length()) {
                 return a < b;
             } else {
                 return a.length() < b.length();
             }
         });
    return result;
}

Solution:
The problem requires a function that takes a vector of strings as input, removes the strings with odd lengths, and returns the resulting vector sorted in ascending order by the length of the strings. If two strings have the same length, they should be sorted alphabetically.

Here's a solution for this problem:

```cpp
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> sorted_list_sum(vector<string> lst) {
    vector<string> result;
    for (string s : lst) {
        if (s.length() % 2 == 0) {
            result.push_back(s);
        }
    }
    sort(result.begin(), result.end(), 
         [](const string& a, const string& b) {
             if (a.length() == b.length()) {
                 return a < b;
             } else {
                 return a.length() < b.length();
             }
         });
    return result;
}
```

The function `sorted_list_sum` takes a vector of strings `lst` as input. It iterates over the input vector and adds the strings with even lengths to the `result` vector. Then, it sorts the `result` vector using a lambda function as the sorting criterion. The lambda function compares two strings `a` and `b`. If they have the same length, it compares them alphabetically. If they have different lengths, it compares them by their lengths. Finally, the function returns the sorted `result` vector. 

This solution passes the given unit tests. For example, `sorted_list_sum({"aa", "a", "aaa"})` returns `{"aa"}` and `sorted_list_sum({"ab", "a", "aaa", "cd"})` returns `{"ab", "cd"}`. 

The time complexity of this solution is O(n log n) due to the sorting operation, where `n` is the number of strings in the input vector. The space complexity is O(n) as we need to store the result in a