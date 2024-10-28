    string s(str.rbegin(),str.rend());
    if (is_palindrome(str))
    return str;
    string res=str;
    while (true){
        int i;
        for (i=str.length()-1;i>=0;i--)
        if (str[i]!=str[i+1])
        break;
        if (i==0){
            res+=str.substr(0,i);
            break;
        }
        str=str.substr(0,i)+str.substr(i+1);
    }
    res+=str.substr(0,i+1)+s.substr(i+1);
    return res;
}

