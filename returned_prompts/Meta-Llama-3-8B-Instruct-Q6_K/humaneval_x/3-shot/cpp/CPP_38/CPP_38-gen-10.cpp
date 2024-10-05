    int l=s.length();
    string output,x;
    int i;
    for (i=0;i*l+l;i++)
    {
        x=s.substr(i*l,l);
        if (x.length()==l) x=x.substr(1)+x[0];
        output=output+x;
    }
    return output;
} 
// test
int main() {
    string s="Hello, world!";
    cout << s << endl;
    cout << encode_cyclic(s) << endl;
    cout << decode_cyclic(encode_cyclic(s)) << endl;
    return 0;
} 
