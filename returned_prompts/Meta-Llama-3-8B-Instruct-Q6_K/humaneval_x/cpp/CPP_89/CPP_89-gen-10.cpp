    string encrypted = "";
    for(int i = 0; i < s.length(); i++){
        char c = s[i];
        if(c >= 'a' && c <= 'z'){
            c = (c - 'a' + 2*2) % 26 + 'a';
        }
        else if(c >= 'A' && c <= 'Z'){
            c = (c - 'A' + 2*2) % 26 + 'A';
        }
        encrypted += c;
    }
    return encrypted;
}

int main(){
    string s = "asdfghjkl";
    string result = encrypt(s);
    printf("%s\n",result.c_str());
    return 0;
}

B:
The function `encrypt` takes a string `s` as an argument and returns a string encrypted with the alphabet being rotated. 
The alphabet should be rotated in a manner such that the letters shift down by two multiplied to two places.

The function iterates over the input string `s`. For each character `c`, it checks if it is a lowercase letter or an uppercase letter. 
If it is a lowercase letter, it subtracts the ASCII value of 'a' from `c`, adds 2*2, takes the modulus with 26 (the number of lowercase letters in the English alphabet), and adds the ASCII value of 'a' back. 
If it is an uppercase letter, it does the same operation but with 'A' instead. 
The encrypted character is then appended to the `encrypted` string.

The `main` function tests the `encrypt` function with the string "asdfghjkl" and prints the result.

Here is the code:

```cpp
#include <iostream>
#include <string>

std::string encrypt(const std::string& s) {
    std::string encrypted;
    for (char c : s) {
        if (c >= 'a' && c <= 'z') {
            c = (c - 'a' + 2*2) % 26 + 'a';
        } else if (c >= 'A' && c <= 'Z') {
            c = (c - 'A' + 2*2) % 26 + 'A';
        }
        encrypted += c;
    }
    return encrypted;
}

int main() {
    std::string s = "asdfghjkl";
    std::string result = encrypt(s);
    std::cout << result << std::endl