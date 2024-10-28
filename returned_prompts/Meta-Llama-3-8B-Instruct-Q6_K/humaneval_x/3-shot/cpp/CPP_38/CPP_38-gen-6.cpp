    string result;
    int l=s.length();
    int num=(l+2)/3;
    int i;
    for (i=0;i<num;i++)
    {
        //cycle elements in each group. Unless group has fewer elements than 3.
        string x=s.substr(i*3,3);
        if (x.length()==3) x=x[2]+x[1]+x[0];
        result+=x;
    }
    return result;
}
// Test
int main() {
    string s = "Hello";
    string encoded = encode_cyclic(s);
    cout << "Encoded: " << encoded << endl;
    string decoded = decode_cyclic(encoded);
    cout << "Decoded: " << decoded << endl;
    return 0;
} 
