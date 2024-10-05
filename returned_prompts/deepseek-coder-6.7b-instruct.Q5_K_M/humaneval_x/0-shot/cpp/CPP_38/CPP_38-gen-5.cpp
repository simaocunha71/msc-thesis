    int l=s.length();
    string output(s);
    for(int i=0;i*3<l;i++)
    {
        //cycle elements in each group. Unless group has fewer elements than 3.
        string x=s.substr(i*3,3);
        if(x.length()==3) x=x[2]+x.substr(0,2);
        output.replace(i*3,3,x);
    }
    return output;
}

int main(){
    string s="HelloWorld";
    string encoded=encode_cyclic(s);
    printf("Encoded string: %s\n",encoded.c_str());
    string decoded=decode_cyclic(encoded);
    printf("Decoded string: %s\n",decoded.c_str());
    return 0;
}

The program reads a string, encodes it with the cyclic encoding function, then decodes it back using the cyclic decoding function. The encoded string is printed to the console, and then the decoded string is printed. The original string and the decoded string should be the same.



