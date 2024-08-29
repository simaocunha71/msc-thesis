#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_set>

using namespace std;

int count_distinct_characters(string str) {
    unordered_set<char> distinct_chars;
    for (char c : str) {
        distinct_chars.insert(tolower(c));
    }
    return distinct_chars.size();
}

int main() {
    cout << count_distinct_characters("xyzXYZ") << endl; // Output: 3
    cout << count_distinct_characters("Jerry") << endl; // Output: 4
    return 0;
}

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_set>

using namespace std;

int count_distinct_characters(string str) {
    unordered_set<char> distinct_chars;
    for (char c : str) {
        distinct_chars.insert(tolower(c));
    }
    return distinct_chars.size();
}

int main() {
    cout << count_distinct_characters("xyzXYZ") << endl; // Output: 3
    cout << count_distinct_characters("Jerry") << endl; // Output: 4
    return 0;
}
```