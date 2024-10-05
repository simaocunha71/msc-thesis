
Here is the C++ code with some corrections:

```cpp
#include<iostream>
#include<string>
using namespace std;

string string_xor(string a, string b){
    string result = "";
    for (int i=0; i<a.length(); i++)
    {
        if (a[i] == b[i])
            result += "0";
        else
            result += "1";
    }
    return result;
}

int main()
{
    string a = "010";
    string b = "110";
    cout<<string_xor(a, b);
    return 0;
}
```

In the function string_xor, the XOR operation is performed on each character of the strings a and b. If the characters are the same, '0' is appended to the result string, otherwise '1' is appended.

In the main function, the function string_xor is called with the strings "010" and "110" as arguments, and the result is printed to the console.

This will output "100", which is the result of the XOR operation on the two input strings.

Note: This code assumes that the input strings a and b are of the same length. If that's not the case, you'll need to handle it accordingly.

I hope this helps. Let me know if you have any questions.


A: This is the corrected code in C++:

```cpp
#include<iostream>
#include<string>
using namespace std;

string string_xor(string a, string b){
   