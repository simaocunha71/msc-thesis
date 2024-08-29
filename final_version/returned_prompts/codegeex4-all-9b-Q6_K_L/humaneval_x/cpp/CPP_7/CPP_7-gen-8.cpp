```cpp
#include <vector>
#include <string>
using namespace std;

vector<string> filter_by_substring(vector<string> strings, string substring) {
    vector<string> result;
    for (string s : strings) {
        if (s.find(substring) != string::npos) {
            result.push_back(s);
        }
    }
    return result;
}
```

Explanation:
The `filter_by_substring` function takes a vector of strings and a substring as input and returns a new vector containing only the strings from the input vector that contain the given substring.

The function iterates over each string in the input vector and checks if the substring is present in the string using the `find` function. If the substring is found, the string is added to the result vector.

Finally, the function returns the result vector containing the filtered strings.