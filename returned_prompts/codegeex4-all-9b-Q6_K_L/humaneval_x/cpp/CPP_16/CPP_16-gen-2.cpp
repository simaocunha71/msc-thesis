```cpp
#include <bits/stdc++.h>
using namespace std;

int count_distinct_characters(string str) {
    // Convert the string to lowercase
    transform(str.begin(), str.end(), str.begin(), ::tolower);
    
    // Initialize a set to store unique characters
    set<char> unique_chars;
    
    // Iterate through each character in the string
    for (char c : str) {
        // Insert each character into the set
        unique_chars.insert(c);
    }
    
    // Return the number of unique characters
    return unique_chars.size();
}

int main() {
    cout << count_distinct_characters("xyzXYZ") << endl;  // Output: 3
    cout << count_distinct_characters("Jerry") << endl;   // Output: 4
    return 0;
}
```
This solution uses a set to store unique characters, and then returns the size of the set. This is a valid approach, as the set data structure automatically handles duplicate characters and only stores unique elements. The `transform` function is used to convert the string to lowercase before processing it.