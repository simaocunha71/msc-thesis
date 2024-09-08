    int max_count = 0;
    string max_word = "";
    for (const auto &word : words) {
        int count = 0;
        set<char> s;
        for (char c : word) {
            s.insert(c);
            if (s.size() > count) {
                count = s.size();
            }
        }
        if (count > max_count) {
            max_count = count;
            max_word = word;
        }
    }
    return max_word;
}

int main() {
    vector<string> words = {"name", "of", "string"};
    string result = find_max(words);
    cout << result << endl;
    return 0;
}

C++:
The task is to find the word with the maximum number of unique characters. If multiple words have the same maximum number of unique characters, the one that comes first in lexicographical order should be returned.

We can solve this task by using the set data structure in C++ to count the unique characters in each word. We iterate through the vector of strings, count the unique characters in each word, and update the maximum count and the corresponding word.

Here is the C++ code that solves the task:

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

string find_max(vector<string> words) {
    int max_count = 0;
    string max_word = "";
    for (const auto &word : words) {
        int count = 0;
        set<char> s;
        for (char c : word) {
            s.insert(c);
            if (s.size() > count) {
                count = s.size();
            }
        }
        if (count > max_count) {
            max_count = count;
            max_word = word;
        }
    }
    return max_word;
}

int main() {
    vector<string> words = {"name", "of", "string"};
    string result = find_max(words);
    cout << result << endl;
    return 0;
}
```

In this code, we define a function `find_max` that takes a vector of strings as input. We initialize `max_count` to 0 and `max_word` to an empty string.

We then iterate through the vector of strings. For each word, we count the unique characters using a set. We update `max_count` and `max_word` if the current word has more unique characters.

Finally,