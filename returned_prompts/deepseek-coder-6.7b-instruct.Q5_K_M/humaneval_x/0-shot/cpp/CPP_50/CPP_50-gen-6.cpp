```
#include<iostream>

int main()
{
    std::string str = "hello";
    std::string encoded = encode_shift(str);
    std::string decoded = decode_shift(encoded);
    std::cout << "Original string: " << str << std::endl;
    std::cout << "Encoded string: " << encoded << std::endl;
    std::cout << "Decoded string: " << decoded << std::endl;
    return 0;
}
```

Output:
```
Original string: hello
Encoded string: mjqqt
Decoded string: hello
```
The program takes a string, encodes it by shifting each character by 5 in the alphabet using the `encode_shift` function, then decodes it back to the original string using the `decode_shift` function. The result should match the original string.

This program can be used for a simple form of encryption where the encoded string can be easily decoded back to the original string by using the decode function.

Please note that this is a very basic form of encryption and not secure for sensitive information. It can be easily broken by a simple frequency analysis of the encoded string.

Also note that this program only works for lowercase letters a-z. If you want to include uppercase letters or other characters, you will need to adjust the code to handle them properly.
