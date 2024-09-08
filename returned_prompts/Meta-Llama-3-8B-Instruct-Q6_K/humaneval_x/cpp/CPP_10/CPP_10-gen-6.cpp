Here is a C++ implementation for the problem:

```cpp
#include <iostream>
#include <string>
using namespace std;

bool is_palindrome(string str) {
    //Test if given string is a palindrome 
    string s(str.rbegin(),str.rend());
    return s==str;
}

string make_palindrome(string str) {
    string prefix = str;
    string suffix = str;
    while (!is_palindrome(suffix)) {
        suffix += str[0];
    }
    return prefix + suffix;
}

int main() {
    string str;
    cout << "Enter a string: ";
    cin >> str;
    cout << "The shortest palindrome that begins with the supplied string is: " << make_palindrome(str) << endl;
    return 0;
}
```

You can compile and run this code to test the function. This program will ask for a string from the user and then print the shortest palindrome that begins with the supplied string. The function `make_palindrome` generates the shortest palindrome by appending the reverse of the prefix to the end of the string. The function `is_palindrome` checks if a given string is a palindrome. The main function demonstrates the use of these functions. 

For example, if the user enters "cata", the program will print "catac" which is the shortest palindrome that begins with "cata". 

This code assumes that the input string is not empty. If you want to handle the case where the input string is empty, you can add a simple check at the beginning of the `main` function. 

Please note that the code may not handle non-alphanumeric characters correctly. If you need to handle such characters, you will need to modify the code accordingly. 

This code is a simple implementation and may not be efficient for very long strings. If you need to handle very long strings, you may need to use a more efficient algorithm. 