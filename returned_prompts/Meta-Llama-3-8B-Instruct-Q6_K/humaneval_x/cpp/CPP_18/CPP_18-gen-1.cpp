    int count = 0;
    int str_len = str.length();
    int substring_len = substring.length();
    for(int i=0; i<=str_len-substring_len; i++){
        if(str.substr(i, substring_len) == substring)
            count++;
    }
    return count;
}

int main() {
    cout << how_many_times("aaa", "a") << endl; // 3
    cout << how_many_times("aaaa", "aa") << endl; // 3
    cout << how_many_times("", "a") << endl; // 0
    return 0;
}

C:
```c
#include <stdio.h>
#include <string.h>

int how_many_times(char *str, char *substring) {
    int count = 0;
    int str_len = strlen(str);
    int substring_len = strlen(substring);
    for(int i=0; i<=str_len-substring_len; i++){
        if(strncmp(str+i, substring, substring_len) == 0)
            count++;
    }
    return count;
}

int main() {
    printf("%d\n", how_many_times("aaa", "a")); // 3
    printf("%d\n", how_many_times("aaaa", "aa")); // 3
    printf("%d\n", how_many_times("", "a")); // 0
    return 0;
}
```

This C code and the Python code do exactly the same thing. They both count the number of times a given substring appears in a string, taking into account overlapping matches.

The C code uses the `strncmp` function to compare substrings, which is similar to Python's `==` operator for strings. The `strlen` function is used to get the length of the strings.

The Python code uses the `==` operator to compare substrings, which is similar to the C code's `strncmp` function. The `len` function is used to get the length of the strings.

Both codes iterate over the original string, checking each substring of the same length as the given substring. If a match is found, the count is incremented. The loop continues until the end of the original string is reached.

The time complexity of both codes is O(n), where n is the length of the original string. This is because each character in the original string is visited at most once during the iteration.

The space complexity of both codes is O(1), which means the space usage does not grow with the size of