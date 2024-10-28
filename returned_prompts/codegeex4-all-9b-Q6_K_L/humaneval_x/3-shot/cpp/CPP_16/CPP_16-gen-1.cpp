    string str1=str;
    sort(str1.begin(),str1.end());
    str1.erase(unique(str1.begin(),str1.end()),str1.end());
    return str1.length();

}

