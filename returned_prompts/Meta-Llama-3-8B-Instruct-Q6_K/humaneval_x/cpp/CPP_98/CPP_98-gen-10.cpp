Here is a simple C++ program that counts the number of uppercase vowels in even indices in a given string.

```cpp
#include <iostream>
#include <string>
using namespace std;

int count_upper(string s) {
    int count = 0;
    for (int i = 0; i < s.size(); i++) {
        if (i % 2 == 0 && (s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U')) {
            count++;
        }
    }
    return count;
}

int main() {
    string s;
    cout << "Enter the string: ";
    cin >> s;
    cout << "The number of uppercase vowels in even indices is: " << count_upper(s) << endl;
    return 0;
}
```

This program works by iterating over the string and checking if the current character is an uppercase vowel and if its index is even. If both conditions are true, it increments the count. Finally, it returns the count.

When you run this program, it will ask you to enter a string. After you enter the string, it will print the number of uppercase vowels in even indices in the string.

Note: This program considers 'A', 'E', 'I', 'O', 'U' as uppercase vowels. It does not consider lowercase vowels. If you want to consider lowercase vowels as well, you can modify the condition in the if statement to check for both lowercase and uppercase vowels.