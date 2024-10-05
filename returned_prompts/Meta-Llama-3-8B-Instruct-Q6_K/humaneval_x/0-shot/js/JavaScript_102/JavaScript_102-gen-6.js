Here is the C++ version of this function:
```cpp
int chooseNum(int x, int y) {
    if (x > y) {
        return -1;
    }
    for (int i = x; i <= y; i++) {
        if (i % 2 == 0) {
            return i;
        }
    }
    return -1;
}
```
Note that the syntax and semantics of the code are similar across languages, but the specific details (such as the use of `range` in Python or `for` loops with variable declarations) may vary