```cpp
#include <unordered_set>
#include <cctype>
#include <string>
using namespace std;

int count_distinct_characters(string str) {
    unordered_set<char> distinct_chars;
    for (char c : str) {
        distinct_chars.insert(tolower(c));
    }
    return distinct_chars.size();
}
```

Explanation:

1. We include the necessary headers and use the namespace std.
2. We define the function count_distinct_characters that takes a string as input.
3. We create an unordered_set named distinct_chars to store the distinct characters.
4. We iterate through each character c in the input string.
5. We convert the character to lowercase using tolower(c) and insert it into the unordered_set.
6. Finally, we return the size of the unordered_set, which represents the number of distinct characters in the string.