    int n=str.size();
    int i=0;
    while(i<n && str[i]==str[n-i-1]) i++;
    if(i==n) return str;
    string t=str.substr(0,i);
    string s(str.rbegin(),str.rbegin()+n-i);
    return s+str+t;
}

