    for(int i = 0; i < str.length(); i++) {
        if(str[i] >= 'a' && str[i] <= 'z') {
            str[i] = str[i] - 32; // Convert to uppercase
        } else if(str[i] >= 'A' && str[i] <= 'Z') {
            str[i] = str[i] + 32; // Convert to lowercase
        }
    }
    return str;
}

int main() {
    string str = "Hello";
    cout << flip_case(str) << endl;
    return 0;
}  // Output: "hELLO"





In this problem, we need to create a function called `flip_case` that takes a string as input and returns the same string but with all lowercase characters converted to uppercase and all uppercase characters converted to lowercase. The function will iterate through each character in the string and apply the conversion if necessary.

Here is the solution in C++:

```cpp
#include <string>
using namespace std;

string flip_case(string str) {
    for(int i = 0; i < str.length(); i++) {
        if(str[i] >= 'a' && str[i] <= 'z') {
            str[i] = str[i] - 32; // Convert to uppercase
        } else if(str[i] >= 'A' && str[i] <= 'Z') {
            str[i] = str[i] + 32; // Convert to lowercase
        }
    }
    return str;
}

int main() {
    string str = "Hello";
    cout << flip_case(str) << endl;
    return 0;
}
```

In this code, we define a function `flip_case` that takes a string `str` as input. We then iterate through each character in the string using a for loop. If the character is a lowercase letter (i.e., its ASCII value is between 'a' and 'z'), we convert it to uppercase by subtracting 32 from its ASCII value. If the character is an uppercase letter (i.e., its ASCII value is between 'A' and 'Z'), we convert it to lowercase by adding 32 to its ASCII value. Finally, we return the modified string.

In the `main` function, we call the `flip_case` function with the string "Hello" and print the result to the console. The output will be "hELLO".