    for (char i : c) {
        s.erase(remove(s.begin(), s.end(), i), s.end());
    }
    string s_rev = s;
    reverse(s_rev.begin(), s_rev.end());
    vector<string> result = {s, s == s_rev ? "True" : "False"};
    return result;
}

int main() {
    vector<string> res;
    res = reverse_delete("abcde", "ae");
    printf("Result: %s %s\n", res[0].c_str(), res[1].c_str());

    res = reverse_delete("abcdef", "b");
    printf("Result: %s %s\n", res[0].c_str(), res[1].c_str());

    res = reverse_delete("abcdedcba", "ab");
    printf("Result: %s %s\n", res[0].c_str(), res[1].c_str());

    return 0;
}
```

This code first removes all characters in `c` from `s` by using the `erase-remove` idiom, then it reverses the string `s` and checks if it equals to the original string `s`. It returns a vector containing the result string and the string "True" if it is palindrome and "False" otherwise.

In the `main` function, it tests the function with the three examples given in the problem statement.

Please note that `remove` does not actually remove the elements from the container, it just moves the elements that are not to be removed to the end of the container and returns an iterator to the new end of the container. That's why we need to call `erase` to actually remove the elements.

Also note that the `std::string::c_str` function is used to convert the string to a C-string so that it can be printed with `printf`.

This code will work in C++11 and later because it uses the range-based `for` loop and the `remove` and `erase` functions from the algorithm library.


R:
```c++
