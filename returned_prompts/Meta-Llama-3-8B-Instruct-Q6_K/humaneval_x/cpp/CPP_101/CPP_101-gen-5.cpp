    vector<string> res;
    // split the string by comma or space
    string temp;
    for (char c : s) {
        if (c == ',' || c == ' ') {
            if (!temp.empty()) {
                res.push_back(temp);
                temp.clear();
            }
        } else {
            temp += c;
        }
    }
    if (!temp.empty()) {
        res.push_back(temp);
    }
    return res;
}

int main() {
    string s1 = "Hi, my name is John";
    string s2 = "One, two, three, four, five, six";
    vector<string> res1 = words_string(s1);
    vector<string> res2 = words_string(s2);
    for (string word : res1) {
        printf("%s ", word.c_str());
    }
    printf("\n");
    for (string word : res2) {
        printf("%s ", word.c_str());
    }
    printf("\n");
    return 0;
}

Output:
Hi my name is John
One two three four five six
Program Explanation:
The program defines a function `words_string` that takes a string as an argument and returns a vector of strings. The function splits the input string into words by comma or space and stores the words in a vector. The words are added to the vector when a comma or space is encountered in the string.

In the `main` function, we test the `words_string` function with two strings `s1` and `s2` and print the output. The output is the vector of words obtained by splitting the input strings. The program uses the `printf` function to print the output. The `c_str` function is used to convert the string to a const char* for printing.

The program uses the `using namespace std;` directive to avoid the need to prefix standard library functions and classes with `std::`. The program also includes the necessary headers (`<iostream>`, `<vector>`, `<string>`) and defines the `words_string` function in the same program.*/



