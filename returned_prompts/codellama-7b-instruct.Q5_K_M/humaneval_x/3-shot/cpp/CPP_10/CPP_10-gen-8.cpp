    int len=str.length();
    int i;
    string longest_palindrome="";
    for (i=0;i<len;i++){
        string prefix=str.substr(0,i);
        string suffix=str.substr(i,len-i);
        if (is_palindrome(suffix))
            longest_palindrome=suffix;
    }
    if (longest_palindrome.length()>0)
        return prefix+reverse(suffix);
    else
        return "";
}



