    int l=s.length();
    int num=(l+2)/3;
    string x,output;
    int i;
    for  (i=0;i*3<l;i++)
    {
        //cycle elements in each group. Unless group has fewer elements than 3.
        x=s.substr(i*3,3);
        if  (x.length()==3) x=x[2]+x.substr(0,2);
        output=output+x;
    }
    return output;
}

int main() {
    string s="ABCDEFG";
    string encoded=encode_cyclic(s);
    printf("Encoded: %s\n", encoded.c_str());
    string decoded=decode_cyclic(encoded);
    printf("Decoded: %s\n", decoded.c_str());
    return 0;
}

The code works for strings of length multiple of 3. If the length of the string is not multiple of 3, then you'll have to add padding to make it so. 

The encode_cyclic function works by splitting the string into groups of three characters, cycling the characters in each group and appending them to the output string. 

The decode_cyclic function does the opposite, it splits the string into groups of three characters, un-cycles the characters in each group and appends them to the output string.

This code does not handle the case where the string length is not a multiple of 3. It will work fine if the string length is a multiple of 3.
*/

//Solution by Sai Charan Reddy Konda
//GitHub: saikonda01
//Email: saikonda01@gmail.com
//Date: 2022-02-08
//Time: 15:00
//Language: C++
//Compile Command: g++ -std=c++11 filename.cpp -o output
//Run Command: ./output
//License: MIT
//Copyright: 2022 Sai Charan Reddy Konda
//Website: https://saikonda.github.