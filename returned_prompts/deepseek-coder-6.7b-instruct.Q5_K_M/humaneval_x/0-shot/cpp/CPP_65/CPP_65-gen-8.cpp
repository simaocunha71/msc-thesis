    string str = to_string(x);
    int len = str.length();
    if (shift >= len) {
        reverse(str.begin(), str.end());
        return str;
    }
    string firstPart = str.substr(0, len-shift);
    string secondPart = str.substr(len-shift, shift);
    return secondPart+firstPart;
}
int main() {
    printf("%s\n", circular_shift(123, 1).c_str());
    printf("%s\n", circular_shift(123, 2).c_str());
    return 0;
}
```

# C++ Solution

```C++
