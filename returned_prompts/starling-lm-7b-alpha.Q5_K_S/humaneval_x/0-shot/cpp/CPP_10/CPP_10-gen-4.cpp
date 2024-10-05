    string str;
    str=str+str.rbegin();
    while(!is_palindrome(str))
        str=str+str[0];
    return str.substr(0,str.length()/2);
}


