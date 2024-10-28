    int l=s.length();
    int num=l/3;
    string x,output;
    int i;
    for  (i=0;i*3<l;i++)
    {
        x=s.substr(i*3,3);
        if  (x.length()==3) x=x[2]+x.substr(0,2);
        output=output+x;
    }
    return output;
}

int main()
{
    string s = "hello world";
    string encoded_s = encode_cyclic(s);
    string decoded_s = decode_cyclic(encoded_s);
    printf("Original string: %s\n", s.c_str());
    printf("Encoded string: %s\n", encoded_s.c_str());
    printf("Decoded string: %s\n", decoded_s.c_str());
    return 0;
}

In your code, you are not handling the case where the length of the string is not a multiple of 3. You are right to do so. However, in your implementation, you are not correctly cycling the characters. You need to shift the characters in the group to the right by one position. The correct code is:

```cpp
string encode_cyclic(string s){ 
    int l=s.length();
    int num=(l+2)/3;
    string x,output;
    int i;
    for  (i=0;i*3<l;i++)
    {
        x=s.substr(i*3,3);
        if  (x.length()==3) x=x[0]+x.substr(1,2);
        output=output+x;
    }
    return output;
}


string decode_cyclic(string s){ 
    int l=s.length();
    int num=l/3;
    string x,output;
    int i;
    for  (i=0;i*3<l;i++)
    {
        x=s.substr(i*3,3);
