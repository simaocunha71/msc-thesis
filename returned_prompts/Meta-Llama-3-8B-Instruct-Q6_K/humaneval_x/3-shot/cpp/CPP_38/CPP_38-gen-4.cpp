    int l=s.length();
    int num=l/3;
    string output;
    int i;
    for (i=0;i<num;i++)
    {
        //reconstruct the groups. The first element of each group will be the last.
        //Unless group has fewer elements than 3.
        output=output+s.substr(i*3,1)+s.substr(i*3+1,2);
    }
    return output;
} 
//main function
int main()
{
    string s="Hello";
    string encode=encode_cyclic(s);
    cout<<encode<<endl;
    string decode=decode_cyclic(encode);
    cout<<decode<<endl;
    return 0;
}
