```cpp
#include <unordered_set>
#include <cctype>
#include <string>

int count_distinct_characters(const std::string& str) {
    std::unordered_set<char> distinct_chars;

    for (char c : str) {
        distinct_chars.insert(std::tolower(c));
    }

    return distinct_chars.size();
}
```

This code defines a function count_distinct_characters that takes a string as an argument and returns the number of distinct characters in the string, ignoring case. It uses a standard unordered_set to store the distinct characters and the tolower function to convert all characters to lowercase before insertion. The size of the set is then returned as the result.