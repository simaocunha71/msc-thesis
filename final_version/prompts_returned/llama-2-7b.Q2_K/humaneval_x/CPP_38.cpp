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
   int i,j,k,l;
    if (s==""){return "";}
    i=0;
	while((i<(int)s.length())&&(s[i]!=' '))++i;
    j=(i+2)/3;
    if (j==-1||j>l){return "";}
    k=i-l;//distance between start of string and the first group. And from this distance, we'll find the length of the last group in the encoded form. 
	int x;
	for (x=0;x<k;++x)
	{
        if ((s[i+x]=='@')||(s[i+x]=='*'))break;//when first character of this position is "@", it indicates that this position will be skipped while decoding. 
    }
	l-=k;//distance from start to position occupied by group in encoded form, that we found by scanning last encoded string. Will used for finding length of string after decoding. 
    l+=x+1;//if group starts with "@" and if it doesn't, add one and divide by 3 to find length of this string after decoding. 
	int y,m,n,o