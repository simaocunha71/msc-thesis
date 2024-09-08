    int m=a.size();
    int n=b.size();
    if(m<n) swap(m,n);
    string res;
    for(int i=0;i<m;i++){
        if(i>=n) res.push_back(a[i]);
        else if(a[i]==b[i]) res.push_back('0');
        else res.push_back('1');
    }
    return res;
}

int main()
{
    string a,b;
    printf("Enter the string a\n");
    cin>>a;
    printf("Enter the string b\n");
    cin>>b;
    string res = string_xor(a,b);
    printf("XOR of two strings is %s\n", res.c_str());
    return 0;
}
