    int i,j;
    int len=str.length();
    for (i=len;i>0;i--){
        string s=str.substr(0,i);
        string s_reverse(s.rbegin(),s.rend());
        if (s==s_reverse) break;
    }
    string s1(str.substr(i,len-i));
    string s2(s1.rbegin(),s1.rend());
    string s3=str+s2;
    return s3;
}

