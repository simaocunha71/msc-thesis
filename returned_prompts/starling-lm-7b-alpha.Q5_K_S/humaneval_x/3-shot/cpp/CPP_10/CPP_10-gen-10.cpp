    string prefix="";
    while (!is_palindrome(str)){
        if (is_palindrome(str.substr(1,str.length()-2)))
        {
        prefix=str.substr(0,1);
        str=str.substr(1,str.length()-2);
        }
        else if (is_palindrome(str.substr(0,str.length()-1)))
        {
        prefix=str.substr(0,str.length()-1);
        str=str.substr(1,str.length()-1);
        }
        else if (is_palindrome(str.substr(0,str.length())))
        {
        prefix=str;
        str="";
        }
        else
        {
        str+=str.substr(0,1);
        str=str.substr(1);
        }
    }
    return prefix+str;
}



