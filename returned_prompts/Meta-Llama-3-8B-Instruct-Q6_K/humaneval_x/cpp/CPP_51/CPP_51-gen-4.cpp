    string result;
    for (int i = 0; i < text.length(); i++) {
        if (text[i] == 'a' || text[i] == 'e' || text[i] == 'i' || text[i] == 'o' || text[i] == 'u' ||
            text[i] == 'A' || text[i] == 'E' || text[i] == 'I' || text[i] == 'O' || text[i] == 'U') {
            continue;
        }
        result += text[i];
    }
    return result;
}

int main() {
    string text = "abcdef\nghijklm";
    cout << remove_vowels(text) << endl;
    return 0;
}

C:
#include <stdio.h>
#include <string.h>

char* remove_vowels(char* text) {
    char* result = malloc(strlen(text) + 1);
    result[0] = '\0';
    for (int i = 0; i < strlen(text); i++) {
        if (text[i] == 'a' || text[i] == 'e' || text[i] == 'i' || text[i] == 'o' || text[i] == 'u' ||
            text[i] == 'A' || text[i] == 'E' || text[i] == 'I' || text[i] == 'O' || text[i] == 'U') {
            continue;
        }
        result = (char*) realloc(result, strlen(result) + 2);
        result[strlen(result)] = text[i];
        result[strlen(result) + 1] = '\0';
    }
    return result;
}

int main() {
    char* text = "abcdef\nghijklm";
    printf("%s\n", remove_vowels(text));
    return 0;
}

R:
```python
def remove_vowels(text):
    return "".join([c for c in text if c.lower() not in "aeiou"])

print(remove_vowels("abcdef\nghijklm"))
```

Python code is more concise and readable. It uses a list comprehension to iterate over each character in the string, and the `join` method to concatenate the characters into a new string. The `lower` method is used to make the code case-insensitive.