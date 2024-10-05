    string str=str;
    string rev=str;
    reverse(rev.begin(), rev.end());
    int i=0;
    while(i<str.length() && str[i]==rev[rev.length()-1-i])
        i++;
    return str+rev.substr(i, rev.length()-i);
}


