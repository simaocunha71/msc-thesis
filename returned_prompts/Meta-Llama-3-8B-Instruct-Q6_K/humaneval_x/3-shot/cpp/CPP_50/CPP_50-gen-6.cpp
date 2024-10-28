    string out;
    int i;
    for (i=0;i<s.length();i++)
    {
        int w=((int)s[i]-(int)'a')%26+(int)'a';   
        out=out+(char)w;
    }
    return out;
}

int main()
{
    string s="hello";
    string encoded=encode_shift(s);
    cout<<encoded<<endl;
    string decoded=decode_shift(encoded);
    cout<<decoded<<endl;
    return 0;
}