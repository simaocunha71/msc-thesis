The function `encode_cyclic` takes a string as input and returns a new string where each group of three characters is rotated by one position to the left. The function `decode_cyclic` does the opposite, rotating each group of three characters to the right. 

Here is the modified code:

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
    for (i=0;i*3<l;i++){
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
    int l=s.length();
    int num=(l+2)/3;
    string x,output;
    int i;
    for (i=0;i*3<l;i++){
        //cycle elements in each group. Unless group has fewer elements than 3.
        x=s.substr(i*3,3);
        if (x.length()==3) x=x.substr(2)+x.substr(0,2);
        output=output+x;
    }
    return output;
}
```

In the `decode_cyclic` function, we rotate each group of three characters to the right by replacing the first two characters with the last two characters. If the group has fewer than three characters, we leave it as is.