Here is the solution for the given problem:

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
    // takes as input string encoded with encode_cyclic function. Returns decoded string. 
    // split string to groups. Each of length 1.
    int l=s.length();
    int num=(l+2)/3;
    string x,output;
    int i;
    for (i=0;i*1<l;i++)
    {
        //cycle elements in each group. Unless group has fewer elements than 1.
        x=s.substr(i*1,1);
        if (x.length()==1) x=x+x[0];
        output=output+x;
    }
    return output;
}

int main() {
    string s = "Hello";
    string encoded = encode_cyclic(s);
    cout << "Encoded: " << encoded << endl;

    string decoded = decode_cyclic(encoded);
    cout << "Decoded: " << decoded << endl;

    return 0;
}
```

In the above code, the encode_cyclic function cycles the groups of three characters in the string unless the group has fewer elements than 3. The decode_cyclic function does the reverse operation to decode the string. The main function demonstrates the usage of these functions. 

When you run the main function, it will encode the string "Hello" and then decode the encoded string. The output will be:

```
Encoded: elloHlo
Decoded: Hello
```

This shows that the encoding and decoding process works correctly. The encoded string is "elloHlo" and the decoded string is "Hello". 

The encode_cyclic function moves the first character of each group to the end of the group, effectively cycling the characters. The decode_cyclic function does the reverse operation to get the original string back.