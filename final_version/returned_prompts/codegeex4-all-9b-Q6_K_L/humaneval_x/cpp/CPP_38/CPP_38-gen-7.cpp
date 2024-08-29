The function `encode_cyclic` works by cycling the characters in groups of three in the input string. Here is how it works:

1. It calculates the length of the input string `s` and the number of groups of three characters. If the length of the string is not a multiple of three, it will add two characters to the length to make it a multiple of three.
2. It then creates an empty string `x` and an empty string `output` to store the characters in each group and the final output, respectively.
3. It loops through the input string in groups of three characters. For each group, it cycles the characters by moving the first character to the end of the group.
4. It then adds the cycled group to the output string.
5. Finally, it returns the output string.

The function `decode_cyclic` works by reversing the process of `encode_cyclic`. It takes as input a string encoded with `encode_cyclic` and returns the original string. Here is how it works:

1. It creates an empty string `output` to store the decoded string.
2. It loops through the input string in groups of three characters. For each group, it cycles the characters by moving the last character to the beginning of the group.
3. It then adds the cycled group to the output string.
4. Finally, it returns the output string.

Here is the complete code:

```cpp
#include<stdio.h>
#include<string>
using namespace std;
string encode_cyclic(string s){ 
    // returns encoded string by cycling groups of three characters.  
    // split string to groups. Each of length 3.
    int l=s.length();
    int num=(l+2)/3;
    string x,output;
    int i;
    for (i=0;i*3<l;i++)
    {
        //cycle elements in each group. Unless group has fewer elements than 3.
        x=s.substr(i*3,3);
        if (x.length()==3) x=x.substr(1)+x[0];
        output=output+x;
    }
    return output;
}


string decode_cyclic(string s){ 
    /*
    takes as input string encoded with encode_cyclic function. Returns decoded string. 
    */
    string output;
    int i;
    for (i=0;i*3<s.length();i++)
    {
        //cycle elements in each group. Unless group has fewer elements than 3.
        string x=s.substr(i*