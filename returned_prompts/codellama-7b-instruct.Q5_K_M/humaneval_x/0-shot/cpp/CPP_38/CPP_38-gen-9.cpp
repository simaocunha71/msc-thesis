#include<stdio.h>
#include<string>
using namespace std;
string decode_cyclic(string s){ 
    // takes as input string encoded with encode_cyclic function. Returns decoded string.
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


int main()
{
    string s="ABCDEFGHIJK";
    cout<<encode_cyclic(s);
    cout<<decode_cyclic(encode_cyclic(s));
    return 0;
}