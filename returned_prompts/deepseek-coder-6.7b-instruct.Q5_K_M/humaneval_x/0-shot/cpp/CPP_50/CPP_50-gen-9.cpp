The problem is that the conversion of the character to its ASCII equivalent is done with the `(int)s[i]`, but the ASCII value of lowercase alphabets are not starting from 0. For instance, 'a' in ASCII has value 97, 'b' has value 98 and so on. So, when you subtract 'a' from an ASCII value of a character, you are subtracting the ASCII value of 'a' from the ASCII value of the character, which will result in a negative value for characters not in the first 26 positions of the alphabet, and a non-sensical result for characters not in the alphabet.

For example, if you try to subtract 'a' from 'c' (which has ASCII value 99), you will get -23, which is not what you want.

To correct this, you should convert the character to its ASCII equivalent by using `int(s[i])`, which will give you the ASCII value of the character.

Here's the corrected code:

```cpp
#include<stdio.h>
#include<string>
using namespace std;
string encode_shift(string s){
    string out;
    int i;
    for  (i=0;i<s.length();i++)
    {
        int w=(int(s[i])+5-int('a'))%26+int('a');   
        out=out+(char)w;
    }
    return out;
}
string decode_shift(string s){
    string out;
    int i;
    for  (i=0;i<s.length();i++)
    {
        int w=(int(s[i])-5-int('a')+26)%26+int('a');   
        out=out+(char)w;
    }
    return out;
}
```

These functions will now correctly encode and decode strings by shifting each character 5 places in the alphabet.

Note: This code assumes that the input string only contains lowercase alphabets. If the input can contain uppercase alphabets or other characters, you will need to