    for(int i=0;str[i] != '\0'; i++){
        if(str[i] >= 'a' && str[i] <= 'z')
            str[i] = str[i] - 32;
        else if(str[i] >= 'A' && str[i] <= 'Z')
            str[i] = str[i] + 32;
    }
    return str;
}
int main(){
    string str;
    cout<<"Enter a string: ";
    cin>>str;
    str = filp_case(str);
    cout<<"Flipped case string is: "<<str;
    return 0;
}
```

The output will be:

```
Enter a string: Hello
Flipped case string is: hELLO
```

In the above program, we are using a for loop to traverse each character in the string. If the character is in lowercase, we subtract 32 from it to convert it to uppercase. If it's in uppercase, we add 32 to convert it to lowercase. At the end, we return the flipped case string.

This program only works for ASCII characters.

**Note:** This solution assumes that the input string is not a multibyte string (a string that contains a character that is encoded in more than one byte).

The solution also assumes that the input string is not null-terminated (a string that does not end with a null character).

In C++, strings are objects and they have their own functions to handle uppercase and lowercase conversions, you can use the `std::transform` function with `std::tolower` and `std::toupper`.

```cpp
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    string str = "Hello";
    transform(str.begin(), str.end(), str.begin(),
        [](unsigned char c){ return islower(c) ? toupper(c) : tolower(c); });
    cout << str;
    return 0;
}
```

This program will output:
