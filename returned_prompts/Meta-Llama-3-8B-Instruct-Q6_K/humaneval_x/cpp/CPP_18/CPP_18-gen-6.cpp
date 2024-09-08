    int count = 0;  // Initialize count of occurrences
    int n = str.length();  // Length of the main string
    int m = substring.length();  // Length of the substring

    // Traverse through the main string
    for (int i = 0; i <= n - m; i++) {
        int j;
        for (j = 0; j < m; j++) {
            // If current character of the main string is not equal to current character of the substring
            if (str[i + j] != substring[j])
                break;
        }
        if (j == m) {
            // If a match is found, increment the count and move the main string by m characters
            count++;
            i += m - 1;  // Move the main string by m characters
        }
    }

    return count;
}
C++


Solution:
Here is the C++ code that counts the number of times a given substring can be found in the original string, including overlapping cases.

```cpp
#include<stdio.h>
#include<string>
using namespace std;

int how_many_times(string str,string substring){
    int count = 0;  // Initialize count of occurrences
    int n = str.length();  // Length of the main string
    int m = substring.length();  // Length of the substring

    // Traverse through the main string
    for (int i = 0; i <= n - m; i++) {
        int j;
        for (j = 0; j < m; j++) {
            // If current character of the main string is not equal to current character of the substring
            if (str[i + j] != substring[j])
                break;
        }
        if (j == m) {
            // If a match is found, increment the count and move the main string by m characters
            count++;
            i += m - 1;  // Move the main string by m characters
        }
    }

    return count;
}
```
In this code, we are using two nested loops to traverse through the main string. The outer loop iterates over the main string, and the inner loop checks if the current substring matches the given substring. If a match is found, we increment the count and move the main string by the length of the substring. This way, we count all occurrences of the substring in the main string, including overlapping cases.

The time complexity of this algorithm is O(n