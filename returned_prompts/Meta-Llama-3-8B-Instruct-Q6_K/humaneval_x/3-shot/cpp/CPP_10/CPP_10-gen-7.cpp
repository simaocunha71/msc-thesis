    string s=str;
    string t;
    int i=str.length()-1;
    while(i>=0 && s[i]==s[0]){
        t=s.substr(1,i);
        s=s.substr(1);
        i--;
    }
    return str+t+string(str.rbegin(),str.rend()).substr(0,t.length());
}

